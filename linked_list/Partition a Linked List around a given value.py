# https://www.geeksforgeeks.org/problems/partition-a-linked-list-around-a-given-value/1
# User function Template for python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def partition(self, head, x):
        # code here
        # we have three buckets
        nodes_less = []
        equal = 0
        nodes_greater = []
        # O(n) traversal to classify each node , then put it in the correct buckets
        ptr = head
        while ptr:
            if ptr.data < x:
                nodes_less.append(ptr)
            elif ptr.data == x:
                equal += 1
            else:
                nodes_greater.append(ptr)
        # link the three buckets
        # Determine the new head
        if nodes_less:
            new_head = nodes_less[0]
        elif equal > 0:
            new_head = Node(x)
            equal -= 1
        elif nodes_greater:
            new_head = nodes_greater[0]
        else:
            return None
        
        current = new_head
        
        # Link remaining nodes less than x
        for node in nodes_less[1:]:
            current.next = node
            current = current.next
        
        # Link all nodes equal to x
        for _ in range(equal):
            current.next = Node(x)
            current = current.next
        
        # Link all nodes greater than x
        for node in nodes_greater:
            current.next = node
            current = current.next
        
        # Terminate the list
        current.next = None
        
        return new_head
