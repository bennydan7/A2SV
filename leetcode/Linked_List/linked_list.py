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
def insert_at_front(head,new_val):
    new_node = Node(new_val)
    new_node.next = head
    return new_node

def insert_at_end(head,new_val):
    new_node = Node(new_val)

    if head == None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    current.next = new_node

    return head


    


def print_list(head):
    current = head

    while current != None:
        print(f"{current.val}", end = " ")
        current = current.next
    
    print()



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

    # print("Count of nodes is",count_nodes(head) )
     # Print the original list
    print("Original Linked List:", end="")
    print_list(head)

    # Insert a new node at the front of the list
    # new_val = 1
    # head = insert_at_front(head, new_val)

    # inserting at the end
    head = insert_at_end(head,1)

    print("After inserting Nodes at the end:", end="")
    print_list(head)
   
if __name__ == "__main__":
    main()

