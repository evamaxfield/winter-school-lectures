import numpy as np
import pytest
from rescale.rescale import rescale


def test_rescale() -> None:
    """Test that rescale works correctly for a simple case."""
    input_array = np.array([1, 2, 3, 4, 5])
    output_array = rescale(input_array)
    expected_array = np.array([0, 0.25, 0.5, 0.75, 1])
    np.testing.assert_allclose(output_array, expected_array)


@pytest.mark.parametrize(
    "input_array, expected_array",
    [
        (np.array([1, 2, 3, 4, 5]), np.array([0, 0.25, 0.5, 0.75, 1])),
        (np.array([5, 4, 3, 2, 1]), np.array([1, 0.75, 0.5, 0.25, 0])),
    ],
)
def test_rescale_parameterized(
    input_array: np.ndarray,
    expected_array: np.ndarray,
) -> None:
    """Test that rescale works correctly for multiple cases."""
    output_array = rescale(input_array)
    np.testing.assert_allclose(output_array, expected_array)


def test_rescale_with_preloaded_data(
    preloaded_data: np.ndarray,
) -> None:
    """Demonstrate how to use fixtures in tests."""
    output_array = rescale(preloaded_data)
    expected_array = np.array([0, 0.5, 0.5, 0.5, 1])
    np.testing.assert_allclose(output_array, expected_array)


# @pytest.mark.parametrize(
#     "input_array",
#     [
#         pytest.param(
#             "some bad value",
#             marks=pytest.mark.xfail(raises=ValueError),
#         ),
#     ],
# )
# def test_rescale_invalid_params(input_array: np.ndarray) -> None:
#     """
#     Test that rescale raises an error when passed invalid parameters.
#     """
#     rescale(input_array)
