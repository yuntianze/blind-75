"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}->{self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the list is empty, return None
        if not lists:
            return None
        # Use divide and conquer to merge lists
        return self.mergeRange(lists, 0, len(lists) - 1)
    
    def mergeRange(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        # If only one list, return it
        if left == right:
            return lists[left]
        # If left > right, return None (invalid range)
        if left > right:
            return None
        # Divide the range into two halves
        mid = (left + right) // 2
        l1 = self.mergeRange(lists, left, mid)
        l2 = self.mergeRange(lists, mid + 1, right)
        # Merge two sorted lists
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge two sorted linked lists
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # Attach the remaining part
        tail.next = l1 if l1 else l2
        return dummy.next

    def list_to_linked_list(self, lst: List[int]) -> Optional[ListNode]:
        # Helper to convert Python list to linked list
        dummy = ListNode()
        tail = dummy
        for val in lst:
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next
    
    

if __name__ == "__main__":
    solution = Solution()
    l1 = solution.list_to_linked_list([1,4,5])
    l2 = solution.list_to_linked_list([1,3,4])
    l3 = solution.list_to_linked_list([2,6])
    merged = solution.mergeKLists([l1, l2, l3])
    # Print merged list
    while merged:
        print(merged.val, end="->" if merged.next else "\n")
        merged = merged.next
  