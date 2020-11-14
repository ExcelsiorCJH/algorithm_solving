"""
Organizing Containers of Balls

Input:
2
3
1 3 1
2 1 2
3 3 3
3
0 2 1
1 1 1
2 0 0

Output:
Impossible
Possible
"""
from collections import Counter


def organizingContainers(container):
    list1 = [sum(row) for row in container]
    list2 = [0] * len(container[0])

    for j in range(len(container[0])):
        for i in range(len(container)):
            list2[j] += container[i][j]

    if Counter(list2) == Counter(list1):
        result = "Possible"
    else:
        result = "Impossible"

    return result


if __name__ == "__main__":
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)