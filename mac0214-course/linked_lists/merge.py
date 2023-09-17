# Problem: https://leetcode.com/problems/merge-two-sorted-lists
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  40ms   / 16.38MB /  a few seconds ago


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = list1
        p2 = list2

        if p2 is None:
            return list1
        
        if p1 is None:
            return list2
        
        before_head = ListNode(-1)
        current = before_head

        while p2 is not None and p1 is not None:
            
            if p2.val <= p1.val:
                current.next = p2
                p2 = p2.next
                current = current.next
                continue
            else:
                current.next = p1
                p1 = p1.next
                current = current.next
                continue

        if p1 is not None:
            current.next = p1

        if p2 is not None:
            current.next = p2
            
        return before_head.next