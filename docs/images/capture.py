"""Create the lecture screenshots in docs/images/ without touching the desktop.

Every screenshot is taken by a headless Edge or Chrome (no window, no mouse, no
keyboard). Terminal screenshots render the real output of real commands.

Usage (from the repository root, with the project's .venv active):
    python docs/images/capture.py 1 2 3 4 5 6
"""
# Developer tool only (not shipped in the package): every command it runs is a fixed list
# built from constants, sys.executable and local paths; it reads no external input.

import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "images"
SOURCES = OUT / "sources"
BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "microsoft-edge",
    "google-chrome",
    "chromium",
]
PORT = 5057
APP = "flask_day_54.presentation.hello"

TERMINAL_CSS = """
body{margin:0;background:#1e1e1e;font-family:Consolas,'DejaVu Sans Mono',monospace;color:#d4d4d4}
.bar{background:#333;color:#ccc;padding:8px 14px;font-size:14px}
pre{margin:0;padding:16px 18px;font-size:15px;line-height:1.45;white-space:pre-wrap}
.p{color:#6a9955}.c{color:#9cdcfe}
"""

BROWSER_CSS = """
body{margin:0;background:#f3f3f3;font-family:Segoe UI,Arial,sans-serif}
.tab{background:#dde3ea;padding:8px 14px;font-size:13px;color:#333}
.url{background:#fff;margin:8px;padding:6px 12px;border:1px solid #bbb;border-radius:14px;font-size:14px}
.page{background:#fff;height:150px;padding:16px;font-size:16px;font-family:Times New Roman,serif}
"""


def find_browser() -> str:
    for candidate in BROWSERS:
        found = shutil.which(candidate) or (candidate if os.path.exists(candidate) else None)
        if found:
            return found
    raise SystemExit("No Edge or Chrome found for headless screenshots")


def shot(page: Path, png: Path, width: int, height: int) -> None:
    """Take a headless screenshot of a local page or a URL."""
    target = page.as_uri() if isinstance(page, Path) else page
    profile = tempfile.mkdtemp(prefix="shot-")
    subprocess.run(  # nosemgrep
        [
            find_browser(),
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--user-data-dir={profile}",
            f"--window-size={width},{height}",
            f"--screenshot={png}",
            "--virtual-time-budget=3000",
            target,
        ],
        check=True,
        capture_output=True,
        timeout=60,
    )
    shutil.rmtree(profile, ignore_errors=True)
    print("wrote", png.relative_to(ROOT))


def run(cmd: list[str], cwd: Path, timeout: int = 30) -> str:
    done = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)  # nosemgrep
    return (done.stdout + done.stderr).rstrip("\n")


def terminal_page(title: str, entries: list[tuple[str, str]], png: Path, height: int) -> None:
    """Render (command, output) pairs as a terminal and take the screenshot."""
    lines = []
    for command, output in entries:
        lines.append(f'<span class="p">$</span> <span class="c">{html.escape(command)}</span>')
        if output:
            lines.append(html.escape(output))
    page = (
        f"<!doctype html><meta charset='utf-8'><style>{TERMINAL_CSS}</style>"
        f"<div class='bar'>{html.escape(title)}</div><pre>" + "\n".join(lines) + "</pre>"
    )
    SOURCES.mkdir(exist_ok=True)
    src = SOURCES / (png.stem + ".html")
    src.write_text(page, encoding="utf-8")
    shot(src, png, 900, height)


def stop(proc: subprocess.Popen) -> None:
    """Stop a server and its reloader child."""
    if os.name == "nt":
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True)  # nosemgrep
    else:
        proc.kill()
    proc.wait(timeout=10)


def python() -> str:
    return sys.executable


def step1() -> None:
    shot(SOURCES / "lecture-01.html", OUT / "lecture-01.png", 900, 400)


def start_server() -> subprocess.Popen:
    proc = subprocess.Popen(  # nosemgrep
        [python(), "-m", "flask", "--app", APP, "run", "--port", str(PORT)],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    for _ in range(40):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{PORT}/", timeout=1).read()
            return proc
        except OSError:
            time.sleep(0.25)  # nosemgrep
    proc.kill()
    raise SystemExit("server did not start")


def step2() -> None:
    proc = start_server()
    try:
        body = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/", timeout=3).read().decode()
        page = (
            f"<!doctype html><meta charset='utf-8'><style>{BROWSER_CSS}</style>"
            f"<div class='tab'>127.0.0.1:5057</div>"
            f"<div class='url'>http://127.0.0.1:{PORT}/</div>"
            f"<div class='page'>{body}</div>"
        )
        src = SOURCES / "lecture-02.html"
        src.write_text(page, encoding="utf-8")
        shot(src, OUT / "lecture-02.png", 700, 230)
    finally:
        stop(proc)


def step3() -> None:
    work = Path(tempfile.mkdtemp(prefix="cli-demo-"))
    bash = shutil.which("bash") or "bash"
    entries = []
    script = [
        "pwd",
        "ls",
        "mkdir my_project",
        "cd my_project && touch hello.py && ls",
        "rm -rf my_project && ls",
    ]
    for command in script:
        output = run([bash, "-c", command], work)
        entries.append((command, re.sub(r"/tmp/cli-demo-\w+", "~/demo", output)))
    shutil.rmtree(work, ignore_errors=True)
    terminal_page("Terminal - lecture 3: the command line", entries, OUT / "lecture-03.png", 330)


def step4() -> None:
    entries = []
    cmd = "python -m flask_day_54.domain.name_demo"
    entries.append((cmd, run([python(), "-m", "flask_day_54.domain.name_demo"], ROOT)))
    imp = "python -c \"import flask_day_54.domain.name_demo as m; print(m.describe_name(m.__name__))\""
    entries.append(
        (
            imp,
            run(
                [
                    python(),
                    "-c",
                    "import flask_day_54.domain.name_demo as m; print(m.describe_name(m.__name__))",
                ],
                ROOT,
            ),
        )
    )
    server = subprocess.Popen(  # nosemgrep
        [python(), "-m", "flask_day_54.presentation.hello"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    time.sleep(3)  # nosemgrep
    stop(server)
    raw = (server.stdout.read() if server.stdout else "").strip()
    # Leave out the .env tip and the random debugger PIN; they say nothing about the lecture.
    kept = [
        line for line in raw.splitlines() if "Tip:" not in line and "Debugger PIN" not in line
    ]
    out = "\n".join(kept)
    entries.append(("python -m flask_day_54.presentation.hello", out + "\n^C"))
    terminal_page("Terminal - lecture 4: __name__ and __main__", entries, OUT / "lecture-04.png", 560)


def step5() -> None:
    module = "flask_day_54.domain.first_class_functions"
    entries = [(f"python -m {module}", run([python(), "-m", module], ROOT))]
    terminal_page("Terminal - lecture 5: functions as first-class objects", entries, OUT / "lecture-05.png", 420)


def step6() -> None:
    module = "flask_day_54.domain.decorators"
    entries = [(f"python -m {module}", run([python(), "-m", module], ROOT))]
    terminal_page("Terminal - lecture 6: decorators and the @ syntax", entries, OUT / "lecture-06.png", 380)


STEPS = {1: step1, 2: step2, 3: step3, 4: step4, 5: step5, 6: step6}

if __name__ == "__main__":
    os.environ["PYTHONPATH"] = str(ROOT / "src")
    for number in [int(a) for a in sys.argv[1:]] or STEPS:
        STEPS[number]()
