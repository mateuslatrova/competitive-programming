# Problem: https://leetcode.com/problems/reorder-list
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  78ms   / 26.26MB /  a few seconds ago


from typing import Optional
from math import ceil

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        dummy_node = ListNode(-1, head)
        nodes_list = [dummy_node]

        current = head

        while (current is not None):
            nodes_list.append(current)
            current = current.next
        
        list_size = len(nodes_list)
    
        half = int(ceil((list_size-1) / 2)) + 1
        
        last_visited_node = dummy_node
        for i in range(1, half):
            
            left = i
            right = list_size-i
            
            left_node = nodes_list[left]
            right_node = nodes_list[right]

            left_node.next = right_node
            last_visited_node.next = left_node

            last_visited_node = right_node

        last_visited_node.next = None
        
        return head

if __name__ == "__main__":
    
    head = ListNode(1, None)
    current = head
    for i in range(2,5):
        new_node = ListNode(i, None)
        current.next = new_node
        current = current.next

    new_head = Solution().reorderList(head)
    
    current = new_head
    while current is not None:
        print(current.val)
        current = current.next

