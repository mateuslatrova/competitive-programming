
# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  32 ms / 16.20 MB /  a few seconds ago

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        last_n_nodes = []

        before_head = ListNode(-1, head)
        p = before_head
        cnt = 0

        while cnt <= n:
            last_n_nodes.append(p)
            p = p.next
            cnt += 1

        while p != None:
            last_n_nodes.pop(0)
            last_n_nodes.append(p)
            p = p.next

        before_node_to_be_removed = last_n_nodes[0]
        node_to_be_removed = last_n_nodes[1]

        before_node_to_be_removed.next = node_to_be_removed.next

        return before_head.next