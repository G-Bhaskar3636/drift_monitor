import pandas as pd

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