from flask_day_54.domain.name_demo import describe_name


def test_describe_name_reports_main_program_when_name_is_main() -> None:
    assert describe_name("__main__") == (
        "Running as the main program: the file was executed directly"
    )


def test_describe_name_reports_imported_module_when_name_is_other() -> None:
    assert describe_name("flask_day_54.domain.name_demo") == (
        "Running as an imported module named flask_day_54.domain.name_demo"
    )


def test_describe_name_reports_imported_module_when_name_is_empty() -> None:
    assert describe_name("") == "Running as an imported module named "
