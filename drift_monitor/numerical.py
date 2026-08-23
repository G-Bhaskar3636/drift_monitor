import numpy as np
from scipy.stats import ks_2samp


def numerical_drift(
    reference,
    current,
    threshold=0.05
):
    """
    Detect numerical drift using
    the Kolmogorov-Smirnov two-sample test.
    """

    # Convert input to NumPy arrays
    reference = np.asarray(reference, dtype=float)
    current = np.asarray(current, dtype=float)

    # Validate empty data
    if len(reference) == 0:
        raise ValueError(
            "Reference data cannot be empty."
        )

    if len(current) == 0:
        raise ValueError(
            "Current data cannot be empty."
        )

    # Validate threshold
    if not 0 < threshold < 1:
        raise ValueError(
            "threshold must be between 0 and 1."
        )

    # Remove NaN values
    reference = reference[~np.isnan(reference)]
    current = current[~np.isnan(current)]

    # Check after removing NaN
    if len(reference) == 0:
        raise ValueError(
            "Reference data contains only NaN values."
        )

    if len(current) == 0:
        raise ValueError(
            "Current data contains only NaN values."
        )

    # Kolmogorov-Smirnov test
    statistic, p_value = ks_2samp(
        reference,
        current
    )

    # Drift decision
    drift_detected = p_value < threshold

    return {
        "statistic": statistic,
        "p_value": p_value,
        "drift_detected": drift_detected
    }