# problem : https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
def has_cycle(head):
    if not head.next:  # empty list
        return False
    else:
        slow = head
        fast = head.next
        while slow and fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
