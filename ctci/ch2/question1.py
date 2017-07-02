def remove_dups(node):
    seen = set()

    prev = None
    curr = node

    while curr:
        if curr.data in seen:
            curr = curr.next
            prev.next = curr
        else:
            seen.add(curr.data)
            prev = curr
            curr = curr.next


def remove_dups_ii(node):
    curr = node
    while curr:
        runner = curr
        while runner.next:
            if curr.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
