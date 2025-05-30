from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        current = head
        while current:
            res.append(current.val)
            current = current.next
        reversi = res[::-1]
        if reversi == res:
            return True
        else:
            return False
        
        