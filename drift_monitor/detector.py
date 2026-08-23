from .numerical import numerical_drift
from .categorical import categorical_drift
from .validation import validate_input


def detect_drift(
    reference,
    current,
    data_type="numerical",
    threshold=0.05
):
    """
    Automatically detect drift based on data type.
    """

    # Validate input
    validate_input(reference, current)

    # Validate threshold
    if not 0 < threshold < 1:
        raise ValueError(
            "threshold must be between 0 and 1."
        )

    # Select detector
    if data_type == "numerical":

        return numerical_drift(
            reference,
            current,
            threshold=threshold
        )

    elif data_type == "categorical":

        return categorical_drift(
            reference,
            current,
            threshold=threshold
        )

    else:
        raise ValueError(
            "data_type must be 'numerical' or 'categorical'."
        )