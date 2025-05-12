from bubble_and_selection import BubbleSortStep


def test_single_item():
    list = []
    assert BubbleSortStep(list) == True
    list2 = [1]
    assert BubbleSortStep(list2) == True
    assert list2[0] == 1


def test_no_swap():
    list = [1, 2]
    assert BubbleSortStep(list) == True
    assert list[0] == 1
    assert list[1] == 2


def test_single_swap():
    list = [1, 3, 2]
    assert BubbleSortStep(list) == False
    assert list[0] == 1
    assert list[1] == 2
    assert list[2] == 3


def test_multiply_swap():
    list = [1, 4, 2, 3]
    assert BubbleSortStep(list) == False
    assert list[0] == 1
    assert list[1] == 2
    assert list[2] == 3
    assert list[3] == 4


def test_multyply_min():
    list = [2, 2, 4, 2]
    assert BubbleSortStep(list) == False
    assert list[0] == 2
    assert list[1] == 2
    assert list[2] == 2
    assert list[3] == 4
