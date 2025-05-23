from insertion_sort import KnuthSequence


def test_empty():
    sequence = KnuthSequence(0)

    assert len(sequence) == 0


def test_single_item():
    sequence = KnuthSequence(1)

    assert len(sequence) == 1
    assert sequence[0] == 1


def test_two_items():
    sequence = KnuthSequence(10)

    assert len(sequence) == 2
    assert sequence[0] == 4
    assert sequence[1] == 1


def test_three_items():
    sequence = KnuthSequence(15)

    assert len(sequence) == 3
    assert sequence[0] == 13
    assert sequence[1] == 4
    assert sequence[2] == 1
