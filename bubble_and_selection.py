from typing import List


def SelectionSortStep(array: List[int], i: int):
    if len(array) < 2:
        return
    if i > (len(array) - 1):
        return

    min_index = i

    for position in range(i + i, len(array)):
        if array[position] < array[i]:
            min_index = position

    if min_index > i:
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp


def BubbleSortStep(array: List[int]) -> bool:
    if len(array) < 2:
        return True

    no_swapped = True

    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
            no_swapped = False

    return no_swapped
