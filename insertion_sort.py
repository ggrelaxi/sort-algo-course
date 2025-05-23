from typing import List


def InsertionSortStep(array: List[int], step: int, i: int):
    if len(array) < 2:
        return
    if i >= len(array):
        return

    for position in range(i, len(array), step):

        prev_position = position
        while (
            prev_position > 0
            and prev_position - step >= 0
            and array[prev_position - step] > array[prev_position]
        ):
            temp = array[prev_position]
            array[prev_position] = array[prev_position - step]
            array[prev_position - step] = temp

            prev_position = prev_position - step


def KnuthSequence(array_size: int):
    if array_size == 0:
        return []

    temp_sequence = []

    base = 1

    while base <= array_size:
        temp_sequence.append(base)
        base = 3 * base + 1

    sequence = []
    for i in range(0, len(temp_sequence)):
        sequence.append(temp_sequence[len(temp_sequence) - i - 1])

    return sequence
