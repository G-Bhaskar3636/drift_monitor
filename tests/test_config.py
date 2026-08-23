import pytest

from drift_monitor.config import MonitorConfig


def test_default_config():

    config = MonitorConfig()

    assert config.drift_threshold == 0.05
    assert config.missing_threshold == 0.20
    assert config.duplicate_threshold == 0.10
    assert config.outlier_multiplier == 1.5


def test_valid_config():

    config = MonitorConfig(
        drift_threshold=0.01,
        missing_threshold=0.10,
        duplicate_threshold=0.05,
        outlier_multiplier=2.0
    )

    config.validate()


def test_invalid_drift_threshold():

    config = MonitorConfig(
        drift_threshold=2
    )

    with pytest.raises(ValueError):
        config.validate()

def test_invalid_missing_threshold():
    config = MonitorConfig(missing_threshold=0)

    with pytest.raises(
        ValueError,
        match="missing_threshold must be between 0 and 1."
    ):
        config.validate()


def test_invalid_duplicate_threshold():
    config = MonitorConfig(duplicate_threshold=1.5)

    with pytest.raises(
        ValueError,
        match="duplicate_threshold must be between 0 and 1."
    ):
        config.validate()


def test_invalid_outlier_multiplier():
    config = MonitorConfig(outlier_multiplier=0)

    with pytest.raises(
        ValueError,
        match="outlier_multiplier must be greater than 0."
    ):
        config.validate()