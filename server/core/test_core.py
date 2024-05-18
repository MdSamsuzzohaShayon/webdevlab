import os
import pytest

# Test function to check the value of PY_ENV
def test_check_py_env():
    # Get the value of PY_ENV environment variable
    py_env_value = os.environ.get('PY_ENV')

    # Assert the expected value of PY_ENV (e.g., 'development', 'production', etc.)
    assert py_env_value is not None, "PY_ENV environment variable is not set"
    assert py_env_value == 'test', f"Unexpected value for PY_ENV: {py_env_value}"
