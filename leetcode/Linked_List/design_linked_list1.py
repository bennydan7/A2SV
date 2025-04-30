class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self,head):
        self.head = None
        self.length = 0

    def get(self,index):
        if index < 0 or index >= self.length:
            return -1
        
        current = self.head
        counter = 0
        while current:
            if counter == index:
                return current.val
            current = current.nextw
            counter += 1
        return -1
    
    def addAtHead(self,val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self,val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def addAtIndex(self,index,val):
        if index <= 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index > self.length:
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self.length += 1


    def deleteAtIndex(self,index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next.next
        current.next = current.next.next
        self.length -= 1
        
    
        

        


