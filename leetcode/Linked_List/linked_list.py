class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


#  Traversing a linked list
def traversing(head):
    current = head
        
    while current != None:
        print(current.val, end= " ")
        current = current.next

# Searching a Linked List
def searching(head,target):
    current = head
    while current != None:
        if current.val == target:
            return True
        
        current = current.next
    return False

# Length of a singly linked List
def count_nodes(head):
    counter = 0
    current = head
    while current != None:
        counter += 1
        current = current.next
    return counter

# insertion in a linked


def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    # Example of traversing the node and printing
    # traversing(head)

    # target = 40
    # if searching(head,target):
    #     print("Yes")
    # else:
    #     print("No")

    print("Count of nodes is",count_nodes(head) )


if __name__ == "__main__":
    main()

