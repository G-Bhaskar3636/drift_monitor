import pandas as pd
import pytest

from drift_monitor.outlier import detect_outliers


def test_outlier_detection():

    df = pd.DataFrame({
        "salary": [
            25000,
            26000,
            27000,
            28000,
            29000,
            30000,
            500000
        ]
    })

    result = detect_outliers(df)

    assert result["salary"]["outlier_count"] == 1


def test_no_outlier():

    df = pd.DataFrame({
        "salary": [
            25000,
            26000,
            27000,
            28000,
            29000,
            30000,
            31000
        ]
    })

    result = detect_outliers(df)

    assert result["salary"]["outlier_count"] == 0


def test_detect_outliers_invalid_input():

    with pytest.raises(
        TypeError,
        match="Input must be a pandas DataFrame."
    ):
        detect_outliers([1, 2, 3, 4])


def test_detect_outliers_empty_dataframe():

    with pytest.raises(
        ValueError,
        match="DataFrame cannot be empty."
    ):
        detect_outliers(pd.DataFrame())


def test_detect_outliers_invalid_multiplier():

    df = pd.DataFrame({
        "age": [10, 20, 30, 40]
    })

    with pytest.raises(
        ValueError,
        match="multiplier must be greater than 0."
    ):
        detect_outliers(df, multiplier=0)


def test_detect_outliers_insufficient_data():

    df = pd.DataFrame({
        "age": [10, 20, 30],
        "name": ["A", "B", "C"]
    })

    result = detect_outliers(df)

    assert result["age"]["status"] == "insufficient_data"
    assert result["age"]["outlier_count"] == 0
    assert result["age"]["outlier_percentage"] == 0.0