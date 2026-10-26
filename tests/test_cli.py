import pytest

from slugkit.__main__ import main


def test_cli_joins_words(capsys):
    assert main(["Hello", "World"]) == 0
    assert capsys.readouterr().out == "hello-world\n"


def test_cli_options(capsys):
    assert main(["-s", "_", "-m", "8", "Hello big World"]) == 0
    assert capsys.readouterr().out == "hello\n"


def test_cli_reports_invalid_options(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["-m", "0", "Hello"])
    assert excinfo.value.code == 2
    assert "max_length" in capsys.readouterr().err
