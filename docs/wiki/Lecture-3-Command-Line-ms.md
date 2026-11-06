# Kuliah 3: Baris arahan

[English](Lecture-3-Command-Line) · [Dansk](Lecture-3-Command-Line-da) · **Bahasa Malaysia**

![Kuliah 3: Baris arahan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-03.png)

## Apa yang dibincangkan dalam kuliah

Terminal berinteraksi dengan kernel sistem pengendalian melalui shell (seperti buah pistachio: kernel ialah isinya, shell ialah kulit luarnya). Ia memberi pembangun kawalan dan kelajuan. Kuliah ini menunjukkan `pwd` (di mana saya), `ls` (apa yang ada di sini), `cd` (pergi ke sana), `mkdir` (folder baharu), `touch` (fail baharu) dan `rm` (padam). `rm -rf` membuang sebuah folder dan segala isinya tanpa bertanya, jadi ia perlu digunakan dengan berhati-hati. Windows mempunyai arahan yang serupa: `cd`, `dir`, `type nul > file`, `del`, `rmdir /s /q`.

## Apa yang kita peroleh

- Enam arahan yang kita gunakan setiap hari untuk bergerak dan mengurus fail.
- Amaran yang jelas untuk dua arahan yang memusnahkan, ditulis dalam kod sebagai data.
- Keyakinan untuk menggunakan terminal dan bukan hanya alat bergrafik.

## Dalam repositori ini

Kod: `src/flask_day_54/domain/cli_basics.py` menyenaraikan arahan beserta bentuknya dalam Windows. Tangkapan skrin menunjukkan arahan sebenar yang dijalankan dalam folder sementara. Ujian: `tests/unit/test_cli_basics.py`.
