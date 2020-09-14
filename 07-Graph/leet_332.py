"""
332. Reconstruct Itinerary

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
"""
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in sorted(tickets):
            graph[start].append(end)

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            result.append(start)

        result = []
        if tickets:
            dfs("JFK")

        return result[::-1]


if __name__ == "__main__":
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    solution = Solution()
    result = solution.findItinerary(tickets)

    print(f"route of tickets: {tickets}\n{result}")
