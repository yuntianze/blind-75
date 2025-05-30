"""
Given the head of a linked list, remove the n^th node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        # Move fast pointer n+1 steps ahead to keep a gap of n between slow and fast
        for _ in range(n + 1):
            fast = fast.next
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        # Remove the target node
        slow.next = slow.next.next
        return dummy.next

# Helper function: convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function: convert linked list to list
def linkedlist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    head1 = list_to_linkedlist([1,2,3,4,5])
    res1 = solution.removeNthFromEnd(head1, 2)
    print(linkedlist_to_list(res1))  # Output: [1,2,3,5]
    # Test case 2
    head2 = list_to_linkedlist([1])
    res2 = solution.removeNthFromEnd(head2, 1)
    print(linkedlist_to_list(res2))  # Output: []
    # Test case 3
    head3 = list_to_linkedlist([1,2])
    res3 = solution.removeNthFromEnd(head3, 1)
    print(linkedlist_to_list(res3))  # Output: [1]


    



