from drift_monitor.categorical import categorical_drift


def test_categorical_drift_detected():

    reference = [
        "A", "A", "A", "A", "A",
        "A", "A", "A", "A", "A"
    ]

    current = [
        "B", "B", "B", "B", "B",
        "B", "B", "B", "B", "B"
    ]

    result = categorical_drift(
        reference,
        current
    )

    assert result["drift_detected"] is True


def test_categorical_no_drift():

    reference = [
        "A", "A",
        "B", "B",
        "C", "C"
    ]

    current = [
        "A", "A",
        "B", "B",
        "C", "C"
    ]

    result = categorical_drift(
        reference,
        current
    )

    assert result["drift_detected"] is False