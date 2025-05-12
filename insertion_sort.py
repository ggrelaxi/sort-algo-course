from typing import List


def InsertionSortStep(array: List[int], step: int, i: int):
    if len(array) < 2:
        return
    if i >= len(array):
        return

    start = 1
    if i != 0:
        start = i

    for position in range(start, len(array), step):
        print("posiition", position)

        prev_position = position
        while (
            prev_position > 0
            and prev_position - step >= 0
            and array[prev_position - step] > array[prev_position]
        ):
            print("before", array)
            temp = array[prev_position]
            array[prev_position] = array[prev_position - step]
            array[prev_position - step] = temp

            prev_position = prev_position - step
            print(array)
