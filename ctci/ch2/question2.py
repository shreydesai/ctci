def kth_to_last(node, k):
    curr = node
    length = 0

    while curr:
        length += 1
        curr = curr.next

    steps = length - k
    curr = node
    for i in range(steps):
        curr = curr.next

    return curr.data


def kth_to_last_ii(node, k):
    curr = node
    runner = node

    for i in range(k - 1):
        runner = runner.next

    while runner.next:
        runner = runner.next
        curr = curr.next

    return curr.data
