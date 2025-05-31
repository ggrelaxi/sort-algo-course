from array_chunk import ArrayChunk


def test_empty():
    list = [1]
    pivot_index = ArrayChunk(list)

    assert pivot_index == 0
    assert list[0] == 1


def test_two_items():
    list = [2, 1]
    pivot_index = ArrayChunk(list)

    assert pivot_index == 0
    assert list[0] == 1
    assert list[1] == 2


def test_multiply_items():
    list = [7, 5, 6, 4, 3, 1, 2]
    pivot_index = ArrayChunk(list)

    assert pivot_index == 3
    assert list == [2, 1, 3, 4, 6, 5, 7]


def test_same_items():
    list = [1, 1, 1]

    pivot_index = ArrayChunk(list)
    assert pivot_index == 1
    assert list == [1, 1, 1]


def test_failed():
    list = [3, 1, 2]

    pivot_index = ArrayChunk(list)

    assert pivot_index == 0
    assert list == [1, 3, 2]
