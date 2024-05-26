# Create by htb on 05/08/2023
# Copyright 2020 AppMillers. All rights reserved

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("the Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search for a node in Singly Linked List
    def searchSLL(self, nodevalue):
        if self.head is None:
            return "the list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return "the value does not exist in this list"
        
    # Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("the SLL doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
        
singlyLinkedList = SlinkedList()

singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(0, 0)

#1. print the singly linked list

print([node.value for node in singlyLinkedList])

#2. traverse Singly linked list

singlyLinkedList.traverseSLL()

#3. Search for a value in SLL

print(singlyLinkedList.searchSLL(3))

#4.
singlyLinkedList.deleteNode(2)
print([node.value for node in singlyLinkedList])