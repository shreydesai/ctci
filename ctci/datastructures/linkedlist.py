class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)
            self.tail = curr.next
        self.count += 1


    def add_list(self, data):
        for d in data:
            self.add(d)


    def string(self):
        nodes = []
        curr = self.head
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.next
        return ' '.join(nodes)
