def palindrome(node):
    stack = []
    curr = node

    while curr:
        stack.append(curr.data)
        curr = curr.next

    curr = node
    while curr:
        if stack.pop() != curr.data:
            return False
        curr = curr.next

    return True


def palindrome_ii(node):
    # Get size of list
    size = 0
    curr = node
    while curr:
        size += 1
        curr = curr.next

    steps = size // 2 - 1

    # Move to middle of list
    curr = node
    while steps > 0:
        curr = curr.next
        steps -= 1

    if size % 2 != 0:
        curr = curr.next

    # Reverse second half of list
    mid = curr
    curr.next = reverse(curr.next)

    # Compare two halves of list
    h1 = node
    h2 = curr.next
    while h2:
        if h1.data != h2.data:
            return False
        h1 = h1.next
        h2 = h2.next

    # Restore list
    mid.next = reverse(mid.next)

    return True


def reverse(node):
    prev = None
    curr = node
    while curr.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    curr.next = prev
    return curr
