from bubble_and_selection import SelectionSortStep


def test_selection_empty_array():
    list = []
    SelectionSortStep(list, 2)
    assert len(list) == 0


def test_single_item():
    list = [5]
    SelectionSortStep(list, 2)
    assert len(list) == 1
    assert list[0] == 5


def test_overflow_index():
    list = [2, 1]
    SelectionSortStep(list, 1)
    assert list[0] == 2
    assert list[1] == 1


def test_success_swap():
    list = [2, 1]
    SelectionSortStep(list, 0)
    assert list[0] == 1
    assert list[1] == 2


def test_success_swap_long_tail():
    list = [4, 3, 2, 1]
    SelectionSortStep(list, 1)
    assert list[1] == 1
    assert list[3] == 3


def test_multiply_min():
    list = [4, 3, 2, 2]
    SelectionSortStep(list, 1)
    assert list[1] == 2
    assert list[2] == 2
    assert list[3] == 3


def test_middle_index():
    list = [1, 2, 3, 10, 8, 7, 5, 6]
    SelectionSortStep(list, 3)
    assert list[3] == 5
    assert list[6] == 10
