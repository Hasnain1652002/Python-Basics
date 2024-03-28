# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0 
        while l1!=None or l2!=None or carry!=0 :
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l1 else 0

            total =l1_val+l2_val+carry
            current.next = ListNode(total%10)
            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l1 else None

            current = current.next
        return head.next