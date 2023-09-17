
# Problem: https://leetcode.com/problems/linked-list-cycle/
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  59ms   / 20.79MB /  a few seconds ago

from collections import defaultdict
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = defaultdict(bool)    

        p = head

        while p is not None:
            if visited[p]:
                return True
            visited[p] = True
            p = p.next

        return False