"""
49 - Group Anagrams
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(word)) for word in strs]

        strs_dict = defaultdict(list)
        for idx, word in enumerate(sorted_strs):
            strs_dict[word].append(idx)

        anagrams = [[strs[idx] for idx in idxs] for idxs in strs_dict.values()]
        return anagrams


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return anagrams.values()
