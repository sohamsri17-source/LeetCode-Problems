# Reversal of Singly Linked List [LeetCode - 206]

class ListNode:
    def __init__(self, info=0, next=None):
        self.data = info
        self.next = next

class Solution:

    def __init__(self, head=None):
        self.head = head 

    def insertAtBeg(self, value):
            temp = ListNode(value)
            temp.next = self.head
            self.head = temp
    
    def reverseList(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next  # Save next before changing
            curr.next = prev       # Reverse current link
            prev = curr            # Move prev forward
            curr = temp       # Move curr forward
        self.head = prev         # Update head to new start

    
    def printlist(self):
        t1 = self.head     # t1 is a tail pointer 
        while(t1.next!=None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = Solution()
obj.insertAtBeg(int(input("Enter the number : ")))
obj.insertAtBeg(int(input("Enter the number : ")))
obj.insertAtBeg(int(input("Enter the number : ")))
obj.insertAtBeg(int(input("Enter the number : ")))
obj.insertAtBeg(int(input("Enter the number : ")))
obj.printlist()

