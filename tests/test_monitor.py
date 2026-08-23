import pandas as pd

from drift_monitor.monitor import monitor_data


def test_monitor_data():

    reference = pd.DataFrame({
        "age": [
            20, 22, 25, 27, 30,
            32, 35, 38, 40, 42
        ],

        "city": [
            "A", "A", "B", "B", "C",
            "C", "A", "B", "C", "A"
        ]
    })

    current = pd.DataFrame({
        "age": [
            50, 52, 55, 58, 60,
            62, 65, 68, 70, 72
        ],

        "city": [
            "A", "A", "B", "B", "C",
            "C", "A", "B", "C", "A"
        ]
    })

    result = monitor_data(
        reference,
        current
    )

    assert "numerical_drift" in result

    assert "categorical_drift" in result

    assert "data_quality" in result

    assert "outliers" in result