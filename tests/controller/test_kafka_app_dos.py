import pytest
from pydantic import ValidationError
from regression_model_template.controller.kafka_app import PredictionRequest, MAX_INPUT_ROWS

def test_prediction_request_max_rows():
    """Test that PredictionRequest enforces max rows limit."""

    # Create input with MAX_INPUT_ROWS + 1 rows
    excessive_rows = MAX_INPUT_ROWS + 1
    input_data = {
        "col1": [i for i in range(excessive_rows)],
        "col2": [i for i in range(excessive_rows)]
    }

    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)

    # Check error message
    assert "Input data exceeds maximum limit" in str(excinfo.value)

def test_prediction_request_valid_rows():
    """Test that PredictionRequest accepts valid rows."""

    # Create input with MAX_INPUT_ROWS rows
    valid_rows = MAX_INPUT_ROWS
    input_data = {
        "col1": [i for i in range(valid_rows)],
        "col2": [i for i in range(valid_rows)]
    }

    request = PredictionRequest(input_data=input_data)
    assert len(request.input_data["col1"]) == valid_rows

def test_prediction_request_empty():
    """Test that PredictionRequest rejects empty input."""

    input_data = {}
    # Assuming empty dict triggers validation error for 'empty' check
    # But wait, InputSchema has default value.
    # If I pass explicit empty dict, validation should catch it.

    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)
    assert "Input data cannot be empty" in str(excinfo.value)

def test_prediction_request_inconsistent_lengths():
    """Test that PredictionRequest rejects inconsistent column lengths."""

    input_data = {
        "col1": [1, 2, 3],
        "col2": [1, 2]  # Different length
    }
    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)
    assert "All columns must have the same length" in str(excinfo.value)
