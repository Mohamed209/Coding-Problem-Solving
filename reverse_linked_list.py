# problem : https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
def reverse(head):
    if not head.next:
        return head
    elif not head:
        return None
    else:
        current_node = head
        while current_node:
            temp_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp_node
            current_node = current_node.prev
        if temp_node:
            temp_node = temp_node.prev
            return temp_node
