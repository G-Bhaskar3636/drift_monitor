from dataclasses import dataclass


@dataclass
class MonitorConfig:
    """
    Configuration for the drift monitoring system.
    """

    drift_threshold: float = 0.05

    missing_threshold: float = 0.20

    duplicate_threshold: float = 0.10

    outlier_multiplier: float = 1.5

    def validate(self):
        """
        Validate configuration values.
        """

        if not 0 < self.drift_threshold < 1:
            raise ValueError(
                "drift_threshold must be between 0 and 1."
            )

        if not 0 < self.missing_threshold <= 1:
            raise ValueError(
                "missing_threshold must be between 0 and 1."
            )

        if not 0 <= self.duplicate_threshold <= 1:
            raise ValueError(
                "duplicate_threshold must be between 0 and 1."
            )

        if self.outlier_multiplier <= 0:
            raise ValueError(
                "outlier_multiplier must be greater than 0."
            )