"""
819 - Most Common Word
"""
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z0-9]", " ", paragraph)
        paragraph = paragraph.split()

        w_dict = Counter(paragraph)
        for ban in banned:
            del w_dict[ban]

        return w_dict.most_common(n=1)[0][0]


class Solution2:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z0-9]", " ", paragraph)
        paragraph = paragraph.split()
        words = [word for word in paragraph if word not in banned]

        words = Counter(words)

        return words.most_common(n=1)[0][0]
