def partition(linkedlist, x):
    curr = linkedlist.head
    linkedlist.tail = linkedlist.head

    while curr:
        # Save next node in order to iterate through
        # the original list
        next_node = curr.next

        if curr.data < x:
            # Add node to head of list
            curr.next = linkedlist.head
            linkedlist.head = curr
        else:
            # Add node to tail of list
            linkedlist.tail.next = curr
            linkedlist.tail = curr
            curr.next = None

        curr = next_node
