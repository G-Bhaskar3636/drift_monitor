from collections import Counter
from scipy.stats import chi2_contingency


def categorical_drift(
    reference,
    current,
    threshold=0.05
):
    """
    Detect categorical drift using
    Chi-Square Test of Independence.
    """

    # Count categories
    reference_counts = Counter(reference)
    current_counts = Counter(current)

    # Get all categories
    categories = set(reference_counts) | set(current_counts)

    # Build contingency table
    reference_freq = [
        reference_counts.get(category, 0)
        for category in categories
    ]

    current_freq = [
        current_counts.get(category, 0)
        for category in categories
    ]

    contingency_table = [
        reference_freq,
        current_freq
    ]

    # Chi-Square Test
    statistic, p_value, _, _ = chi2_contingency(
        contingency_table
    )

    # Detect drift
    drift_detected = p_value < threshold

    return {
        "statistic": statistic,
        "p_value": p_value,
        "drift_detected": bool(drift_detected)
    }