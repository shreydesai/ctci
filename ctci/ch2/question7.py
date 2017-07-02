def intersection(a, b):
    # Determine if intersection exists
    tail_a, tail_b = a, b
    size_a, size_b = 1, 1
    while tail_a.next or tail_b.next:
        if tail_a.next:
            tail_a = tail_a.next
            size_a += 1
        if tail_b.next:
            tail_b = tail_b.next
            size_b += 1

    # Tails are not the same, so an intersection
    # between the lists doesn't exist
    if tail_a is not tail_b:
        return None

    # Determine shorter/longer list
    short_node = a if size_a < size_b else b
    long_node = b if size_a < size_b else a

    # Fast forward longer list
    for i in range(abs(size_a - size_b)):
        long_node = long_node.next

    # Compare nodes until we reach common one
    while short_node is not long_node:
        short_node = short_node.next
        long_node = long_node.next

    return short_node
