import pytest
import numpy as np

@pytest.fixture
def preloaded_data():
    return np.array([-1, 0, 0, 0, 1])