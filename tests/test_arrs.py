from utils import arrs
import pytest


@pytest.mark.parametrize('array_, index_, default_, result',
                         [([1, 2, 3], 1, "test", 2),
                          ([], 0, "test", "test")])
def test_get(array_, index_, default_, result):
    assert arrs.get(array_, index_, default_) == result


@pytest.mark.parametrize('arr, start, end, res',
                         [([1, 2, 3, 4], 1, 3, [2, 3]),
                          ([1, 2, 3], 1, None, [2, 3])])
def test_slice(arr, start, end, res):
    assert arrs.my_slice(arr, start, end) == res
