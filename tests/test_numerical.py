import numpy as np
import pytest

from drift_monitor.numerical import numerical_drift


def test_numerical_drift_detected():

    reference = [
        10, 12, 11, 13, 12,
        14, 15, 13, 11, 12
    ]

    current = [
        50, 55, 52, 60, 58,
        62, 65, 61, 59, 64
    ]

    result = numerical_drift(
        reference,
        current
    )

    assert result["drift_detected"] is True


def test_numerical_no_drift():

    reference = [
        10, 12, 11, 13, 12,
        14, 15, 13, 11, 12
    ]

    current = [
        10, 11, 12, 13, 14,
        15, 12, 11, 13, 12
    ]

    result = numerical_drift(
        reference,
        current
    )

    assert result["drift_detected"] is False


def test_empty_reference():

    with pytest.raises(ValueError):

        numerical_drift(
            [],
            [1, 2, 3]
        )


def test_invalid_threshold():

    with pytest.raises(ValueError):

        numerical_drift(
            [1, 2, 3],
            [4, 5, 6],
            threshold=2
        )

def test_numerical_drift_invalid_threshold():

    reference = [1, 2, 3, 4]
    current = [1, 2, 3, 4]

    with pytest.raises(
        ValueError,
        match="threshold must be between 0 and 1."
    ):
        numerical_drift(
            reference,
            current,
            threshold=0
        )


def test_numerical_drift_reference_only_nan():

    reference = [np.nan, np.nan, np.nan]
    current = [1, 2, 3]

    with pytest.raises(
        ValueError,
        match="Reference data contains only NaN values."
    ):
        numerical_drift(
            reference,
            current
        )


def test_numerical_drift_current_only_nan():

    reference = [1, 2, 3]
    current = [np.nan, np.nan, np.nan]

    with pytest.raises(
        ValueError,
        match="Current data contains only NaN values."
    ):
        numerical_drift(
            reference,
            current
        )