"""
234. Palindrome Linked List
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        # Runner를 이용해 역순 Linked List 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # 홀수일 경우
        if fast:
            slow = slow.next

        # 팰린드롬 판별
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev
