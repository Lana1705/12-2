from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 7, 9], 0, "test") == 1
    assert arrs.get([1, 2, 5], 2, "test") == 5
    assert arrs.get([1, 2, 5], -2, "None") == "None"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]
