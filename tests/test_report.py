from pathlib import Path

from drift_monitor.report import generate_html_report


def test_generate_html_report(tmp_path):

    report = {
        "numerical_drift": {
            "age": {
                "drift_detected": True,
                "p_value": 0.01
            }
        },

        "categorical_drift": {},

        "data_quality": {
            "status": "good",
            "rows": 100,
            "columns": 5,
            "duplicate_rows": 2
        },

        "outliers": {
            "age": {
                "outlier_count": 3,
                "outlier_percentage": 3.0
            }
        }
    }

    output_file = tmp_path / "report.html"

    result = generate_html_report(
        report,
        output_file
    )

    assert result == output_file
    assert output_file.exists()

    content = output_file.read_text(
        encoding="utf-8"
    )

    assert "Drift Monitor Report" in content
    assert "age" in content
    assert "DRIFT" in content
    assert "good" in content