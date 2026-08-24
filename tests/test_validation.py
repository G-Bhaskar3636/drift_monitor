import pytest

from drift_monitor.validation import validate_input


def test_validate_input_valid():
    assert validate_input([1, 2, 3], [4, 5, 6]) is True


def test_reference_none():
    with pytest.raises(ValueError, match="Reference data cannot be None."):
        validate_input(None, [1, 2, 3])


def test_current_none():
    with pytest.raises(ValueError, match="Current data cannot be None."):
        validate_input([1, 2, 3], None)


def test_reference_empty():
    with pytest.raises(ValueError, match="Reference data cannot be empty."):
        validate_input([], [1, 2, 3])


def test_current_empty():
    with pytest.raises(ValueError, match="Current data cannot be empty."):
        validate_input([1, 2, 3], [])


def test_reference_not_iterable():
    with pytest.raises(TypeError):
        validate_input(123, [1, 2, 3])


def test_current_not_iterable():
    with pytest.raises(TypeError):
        validate_input([1, 2, 3], 123)

def test_validation_string_input():
    with pytest.raises(TypeError):
        validate_input("invalid_str", [1, 2, 3])


def test_validation_invalid_type():
    with pytest.raises(TypeError):
        validate_input([1, 2, 3], "invalid_str")