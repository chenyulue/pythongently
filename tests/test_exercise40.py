import pytest

from ppeg.exercise40 import merge_two_lists

@pytest.mark.parametrize("list1, list2, expected", [
    ([1,3,6],[5,7,8,9],[1,3,5,6,7,8,9]),
    ([1,2,3],[4,5],[1,2,3,4,5]),
    ([4,5],[1,2,3],[1,2,3,4,5]),
    ([2,2,2],[2,2,2],[2,2,2,2,2,2]),
    ([1,2,3],[], [1,2,3]),
    ([],[1,2,3],[1,2,3])
])
def test_merge_two_lists(list1, list2, expected):
    assert merge_two_lists(list1, list2) == expected