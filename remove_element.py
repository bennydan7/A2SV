class ListNode:
    def __init__(self,head,next):
        self.head = head
        self.next = None
    
def removeElements(self,head:ListNode,val:int):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current and current.next:
        if current.next.val==val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy


print(removeElements(1,head=[1,2,6,3,4,5,6],val=6))