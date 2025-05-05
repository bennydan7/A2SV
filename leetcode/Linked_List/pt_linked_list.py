class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # insert in Linked List
    def insert_single_linkedlist(self,value,location):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

        
    def traverse_singly_linkedlist(self):
        if self.head == None:
            print("Linked list doesn't exist")
        else:
            node = self.head
            while node != None:
                print(node.value)
                node = node.next


    

singlyLinkedList = SLinkedList()
singlyLinkedList.insert_single_linkedlist(1,1)
singlyLinkedList.insert_single_linkedlist(2,1)
singlyLinkedList.insert_single_linkedlist(3,1)
singlyLinkedList.insert_single_linkedlist(4,1)


singlyLinkedList.insert_single_linkedlist(0,0)
singlyLinkedList.insert_single_linkedlist(0,3)

print([node.value for node in singlyLinkedList])

singlyLinkedList.traverse_singly_linkedlist()