import pandas as pd
import pytest

from drift_monitor.quality import data_quality_report


def test_quality_pass():

    df = pd.DataFrame({
        "age": [20, 25, 30, 35, 40],
        "salary": [25000, 30000, 35000, 40000, 45000]
    })

    result = data_quality_report(df)

    assert result["status"] == "pass"


def test_quality_missing_values():

    df = pd.DataFrame({
        "age": [
            20,
            None,
            None,
            None,
            40
        ]
    })

    result = data_quality_report(
        df,
        missing_threshold=0.20
    )

    assert result["status"] == "fail"


def test_empty_dataframe():

    df = pd.DataFrame()

    with pytest.raises(ValueError):

        data_quality_report(df)