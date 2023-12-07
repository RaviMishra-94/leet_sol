from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            temp_sum = x + y + carry

            current.next = ListNode(temp_sum % 10)
            carry = temp_sum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next

        return dummy_head.next
