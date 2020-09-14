"""
207. Course Schedule
Key point: DFS를 이용한 순환 구조 check
"""

from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(v):
            # 순환구조일 경우
            if v in traced:
                return False
            # 이미 방문한 노드
            if v in visited:
                return True

            traced.add(v)
            for w in graph[v]:
                if not dfs(w):
                    return False

            traced.remove(v)
            visited.add(v)
            return True

        traced = set()
        visited = set()

        graph = defaultdict(list)
        for s, e in prerequisites:
            graph[s].append(e)

        for v in list(graph):
            if not dfs(v):
                return False

        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)

    print(f"result of {prerequisites}:\n{result}")
