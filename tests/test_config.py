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