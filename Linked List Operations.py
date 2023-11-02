# Linked list operations in Python

#Create a node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    #Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head  # the initial head (first node) now becomes the second node
        self.head = new_node #the new node inserted becomes the head

    #Insert after a node
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next  #the node after the newly inserted node is the node that is right after the node the newly added node was added next to
        prev_node.next = new_node # the new node is placed after the node that it has to be placed after.
        
    #Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node  # if there are no nodes (and thus head), the new node is the head
            return
        
        last = self.head
        while(last.next):
            last = last.next  # while there is a next node after this current node, all nodes are brought forward

        last.next = new_node  # new node is inserted at the ned

    #Deleting a node
    def deleteNode(self, position):

        if self.head is None:  # if there are no nodes, we can't delete any nodes
            return 
        
        temp = self.head

        if position == 0:
            self.head = temp.next  # if the first node (head) is to be deleted, the 2nd node becomes the head node
            temp = None
            return
        
        #Find the key to be deleted
        for i in range(position -1):  
            temp = temp.next  # if any other nodes are to be deleted, 
            if temp is None:
                break

        #If the key is not present
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next
    

    #Search an element
    def search(self, key):

        current = self.head
    
        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False
    

    #Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                #index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    #Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end=" ")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find)+ " is found")
    else:
        print(str(item_to_find)+ " is not found")
    
    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()


class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
  
# Function to insert a new node at the beginning
def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
  
# Utility function to print the LinkedList
def printList(self):
    temp = self.head
    while(temp):
        print (temp.data,end=" ")
        temp = temp.next
  
  
# Driver program to test above functions
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
  
print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()