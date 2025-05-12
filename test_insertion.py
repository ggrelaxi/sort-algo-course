from insertion_sort import InsertionSortStep


def test_small_array_case():
    list = [1]
    InsertionSortStep(list, 1, 0)
    assert list[0] == 1

    list2 = [1, 2]
    InsertionSortStep(list2, 1, 0)
    assert list2[0] == 1
    assert list2[1] == 2

    list3 = [2, 1]
    InsertionSortStep(list3, 1, 0)
    assert list3[0] == 1
    assert list3[1] == 2


def test_index_out_range_case():
    list = [2, 1]
    InsertionSortStep(list, 1, 2)
    assert list[0] == 2
    assert list[1] == 1


def test_single_step_case():
    list = [4, 3, 1, 2]
    InsertionSortStep(list, 1, 1)
    assert list[0] == 1
    assert list[1] == 2
    assert list[2] == 3
    assert list[3] == 4


def test_success_step_case():
    list = [1, 6, 5, 4, 3, 2, 7]
    step = 3
    i = 1
    InsertionSortStep(list, step, i)

    assert list[0] == 1
    assert list[1] == 3
    assert list[2] == 5
    assert list[3] == 4
    assert list[4] == 6
    assert list[5] == 2
    assert list[6] == 7
