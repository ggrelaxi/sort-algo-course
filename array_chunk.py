from typing import List


def ArrayChunk(M: List[int]):
    pivot_index = len(M) // 2
    N = M[pivot_index]

    i1 = -1
    i2 = len(M)

    while True:
        i1 += 1

        while M[i1] < N:
            i1 += 1

        i2 -= 1

        while M[i2] > N:
            i2 -= 1

        if i1 >= i2:
            return pivot_index

        M[i1], M[i2] = M[i2], M[i1]
