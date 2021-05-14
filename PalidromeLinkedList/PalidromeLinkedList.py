'''
Cracking the coding interview
Chapter 2 - Linked List pg 94
Linked List - Palidrome
----------------------------------------
Question: Implement a function to check if a linked list is a palidrome
Example: 
input: r->a->c->e->c->a->r->None
output: True because its the same word backwards and forward
Constraits or Questions you need to ask:
- Try brute force method. 
- Print the values of the linked list into an array
- Check the array if the items inside are a palidrome
Solution notes:
- Initalize an empty array
- run while loop to traverse through linked list and print into array
- reverse the array and check if the array is equal to the revered array

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    #Brute force method
    def isPalidrome(self):
        #Intialize an empty array
        elements = []
        #intialize a pointer to the head of the linked list
        cur = self.head
        while cur:
            #While iterating, add values to the array
            elements.append(cur.data)
            #Iterate to the next node
            cur = cur.next
        print(elements)
        #New array that has the reverse of the OG array, slicing
        reversedArray = elements[::-1]
        print(reversedArray)
        #If the reverse == to the original its a palidrome
        if elements == reversedArray:
            print("The linked list is a palidrome")
        else:
            print("The linked list is NOT a palidrome")


    #Method 2: Using O(n) Time and O(1) Space
    def Palidrom(self):
        #Using 2 pointers to detirmine the middle
        fast = self.head
        slow = self.head

        #Finding the middle using (slow ptr)
        while fast and fast.next:
            #Fast moves 2x and Slow moves 1x
            fast = fast.next.next
            slow = slow.next

        #Reverse second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        #Check if it's a palidrome
        left, right = self.head , prev
        while right:
            if left.data != right.data:
                print("Not a palidrome")
                return
            left = left.next
            right = right.next
        print("Palidrome!")
        return 
       

      
        
list1 = LinkedList()

list1.append('r')
list1.append('a')
list1.append('c')
list1.append('e')
list1.append('c')
list1.append('a')
list1.append('r')


list2 = LinkedList()

list2.append(1)
list2.append(2)
list2.append(3)
list2.append(4)
list2.append(5)

#list1.isPalidrome()
#list1.Palidrom()
list2.isPalidrome()
list2.Palidrom()