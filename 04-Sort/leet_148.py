"""
148. Sort List
"""

from typing import TypeVar

ListNode = TypeVar("ListNode")

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortList(self, head: ListNode) -> ListNode:
            # LinkedList -> python list
            p = head
            lst = []
            while p:
                lst.append(p.val)
                p = p.next

            # sort
            lst.sort()

            # python list -> LinkedList
            p = head
            for el in lst:
                p.val = el
                p = p.next
            return head