"""
HackerRank - The Grid Search
"""
import re


def gridSearch(G, P):
    l = len(P)
    m = len(P[0])
    for x, y in enumerate(G):
        for i in ((m.start(0)) for m in re.finditer("(?=%s)" % P[0], y)):
            for a in range(1, l):
                if G[a + x][i : i + m] != P[a]:
                    break
            else:
                return "YES"

    return "NO"


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)