import numpy as np
import pytest


@pytest.fixture
def preloaded_data() -> np.ndarray:
    """
    Demonstrate how to use fixtures in tests.

    Fixtures are useful if you want to load a resource once and then use it
    in multiple tests. This is especially useful if loading the resource
    takes a long time.
    """
    return np.array([-1, 0, 0, 0, 1])
