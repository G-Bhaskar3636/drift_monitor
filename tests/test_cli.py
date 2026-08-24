import pytest
from unittest.mock import patch, MagicMock
from drift_monitor.cli import main


def test_cli_no_args(capsys):
    """Test running CLI without arguments (prints help)."""
    with patch("sys.argv", ["drift-monitor"]):
        main()
    captured = capsys.readouterr()
    assert "usage: drift-monitor" in captured.out or "ML data drift" in captured.out


def test_cli_version(capsys):
    """Test running CLI with --version."""
    with patch("sys.argv", ["drift-monitor", "--version"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "drift-monitor 0.1.0" in captured.out or "drift-monitor 0.1.0" in captured.err


@patch("drift_monitor.cli.generate_html_report")
@patch("drift_monitor.cli.print_report")
@patch("drift_monitor.cli.monitor_data")
@patch("pandas.read_csv")
def test_cli_check_command_without_output(mock_read_csv, mock_monitor, mock_print, mock_html):
    """Test running 'drift-monitor check --reference ref.csv --current cur.csv'."""
    mock_df_ref = MagicMock()
    mock_df_cur = MagicMock()
    mock_read_csv.side_effect = [mock_df_ref, mock_df_cur]
    mock_report = {"drift_summary": "ok"}
    mock_monitor.return_value = mock_report

    test_args = [
        "drift-monitor",
        "check",
        "--reference", "ref.csv",
        "--current", "cur.csv"
    ]

    with patch("sys.argv", test_args):
        main()

    # Verify CSVs were loaded
    assert mock_read_csv.call_count == 2
    mock_read_csv.assert_any_call("ref.csv")
    mock_read_csv.assert_any_call("cur.csv")

    # Verify monitor and print functions were called
    mock_monitor.assert_called_once_with(mock_df_ref, mock_df_cur)
    mock_print.assert_called_once_with(mock_report)
    mock_html.assert_not_called()


@patch("drift_monitor.cli.generate_html_report")
@patch("drift_monitor.cli.print_report")
@patch("drift_monitor.cli.monitor_data")
@patch("pandas.read_csv")
def test_cli_check_command_with_output(mock_read_csv, mock_monitor, mock_print, mock_html, capsys):
    """Test running 'drift-monitor check' with optional --output flag."""
    mock_df_ref = MagicMock()
    mock_df_cur = MagicMock()
    mock_read_csv.side_effect = [mock_df_ref, mock_df_cur]
    mock_report = {"drift_summary": "ok"}
    mock_monitor.return_value = mock_report
    mock_html.return_value = "report.html"

    test_args = [
        "drift-monitor",
        "check",
        "--reference", "ref.csv",
        "--current", "cur.csv",
        "--output", "report.html"
    ]

    with patch("sys.argv", test_args):
        main()

    # Verify HTML generation was triggered
    mock_html.assert_called_once_with(mock_report, "report.html")

    captured = capsys.readouterr()
    assert "HTML report saved to: report.html" in captured.out