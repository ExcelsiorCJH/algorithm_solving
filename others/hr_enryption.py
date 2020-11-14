"""
HackerRank - Encryption

Input:
haveaniceday

Output:
hae and via ecy
"""
import math


def encryption(s):
    if len(s) <= 1:
        return s

    s_sqrt = math.sqrt(len(s))
    ncol = math.ceil(s_sqrt)
    nrow = math.floor(s_sqrt)

    if nrow * ncol < len(s):
        nrow += 1

    M = []
    start = 0
    for i in range(nrow):
        M.append(s[start : ncol * (i + 1)])
        start += ncol

    if len(M[-1]) < len(M[-2]):
        M[-1] += " " * (len(M[-2]) - len(M[-1]))

    MT = []
    for j in range(ncol):
        tmp = ""
        for i in range(nrow):
            tmp += M[i][j]
        MT.append(tmp.strip())

    return " ".join(MT)


if __name__ == "__main__":
    s = input()

    result = encryption(s)
    print(result)