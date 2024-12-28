import random

from ppeg.exercise38 import shuffle

random.seed(42)

def test_shuffle_with_nonempty_list():
    for i in range(10):
        test_data1 = [1,2,3,4,5,6,7,8,9,10]
        shuffle(test_data1)

        assert len(test_data1) == 10
        assert test_data1 != [1,2,3,4,5,6,7,8,9,10]
        assert sorted(test_data1) == [1,2,3,4,5,6,7,8,9,10]

def test_shuffle_with_empty_list():
    test_data2 = []
    shuffle(test_data2)
    assert test_data2 == []