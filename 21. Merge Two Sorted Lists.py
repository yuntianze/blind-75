"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        tail = dummy
        # Iterate while both lists are not empty
        while list1 and list2:
            # Compare the values of the current nodes
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # Attach the remaining part of the non-empty list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        # Return the merged list, skipping the dummy node
        return dummy.next
    

def list_to_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

    

if __name__ == "__main__":
    solution = Solution()
    print(linked_list_to_list(solution.mergeTwoLists(list_to_linked_list([1,2,4]), list_to_linked_list([1,3,4]))))
    print(linked_list_to_list(solution.mergeTwoLists(list_to_linked_list([]), list_to_linked_list([]))))
    print(linked_list_to_list(solution.mergeTwoLists(list_to_linked_list([]), list_to_linked_list([0]))))
    
