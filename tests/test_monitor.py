import pandas as pd
import pytest

from drift_monitor.monitor import monitor_data
from drift_monitor.config import MonitorConfig


def test_monitor_with_drift():

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

    result = monitor_data(reference, current)

    assert "numerical_drift" in result
    assert "categorical_drift" in result
    assert "data_quality" in result
    assert "outliers" in result

    assert "age" in result["numerical_drift"]
    assert "city" in result["categorical_drift"]


def test_monitor_no_drift():

    reference = pd.DataFrame({
        "age": [20, 21, 22, 23, 24],
        "city": [
            "Hyderabad",
            "Delhi",
            "Mumbai",
            "Delhi",
            "Hyderabad"
        ]
    })

    current = pd.DataFrame({
        "age": [20, 21, 22, 23, 24],
        "city": [
            "Hyderabad",
            "Delhi",
            "Mumbai",
            "Delhi",
            "Hyderabad"
        ]
    })

    result = monitor_data(reference, current)

    assert "numerical_drift" in result
    assert "categorical_drift" in result
    assert "data_quality" in result
    assert "outliers" in result


def test_monitor_invalid_reference():

    current = pd.DataFrame({
        "age": [20, 21, 22]
    })

    with pytest.raises(
        TypeError,
        match="Reference data must be a pandas DataFrame."
    ):
        monitor_data([1, 2, 3], current)


def test_monitor_invalid_current():

    reference = pd.DataFrame({
        "age": [20, 21, 22]
    })

    with pytest.raises(
        TypeError,
        match="Current data must be a pandas DataFrame."
    ):
        monitor_data(reference, [1, 2, 3])


def test_monitor_empty_reference():

    reference = pd.DataFrame()

    current = pd.DataFrame({
        "age": [20, 21, 22]
    })

    with pytest.raises(
        ValueError,
        match="Reference DataFrame cannot be empty."
    ):
        monitor_data(reference, current)


def test_monitor_empty_current():

    reference = pd.DataFrame({
        "age": [20, 21, 22]
    })

    current = pd.DataFrame()

    with pytest.raises(
        ValueError,
        match="Current DataFrame cannot be empty."
    ):
        monitor_data(reference, current)


def test_monitor_missing_column():

    reference = pd.DataFrame({
        "age": [20, 21, 22, 23],
        "salary": [25000, 26000, 27000, 28000]
    })

    current = pd.DataFrame({
        "age": [20, 21, 22, 23]
    })

    result = monitor_data(reference, current)

    assert "age" in result["numerical_drift"]
    assert "salary" not in result["numerical_drift"]


def test_monitor_with_outliers():

    reference = pd.DataFrame({
        "age": [20, 21, 22, 23, 24]
    })

    current = pd.DataFrame({
        "age": [20, 21, 22, 23, 500]
    })

    result = monitor_data(reference, current)

    assert "age" in result["outliers"]


def test_monitor_invalid_config():

    reference = pd.DataFrame({
        "age": [20, 21, 22, 23]
    })

    current = pd.DataFrame({
        "age": [20, 21, 22, 23]
    })

    config = MonitorConfig(
        drift_threshold=0
    )

    with pytest.raises(
        ValueError,
        match="drift_threshold must be between 0 and 1."
    ):
        monitor_data(
            reference,
            current,
            config=config
        )