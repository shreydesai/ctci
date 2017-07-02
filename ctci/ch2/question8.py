def loop_detection(node):
    slow, fast = node, node

    # Determine if list has cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    if fast.next is None:
        return None

    # Catch up with fast node
    slow = node
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow
