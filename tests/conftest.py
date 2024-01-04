import numpy as np
import pytest


@pytest.fixture
def preloaded_data() -> np.ndarray:
    return np.array([-1, 0, 0, 0, 1])
