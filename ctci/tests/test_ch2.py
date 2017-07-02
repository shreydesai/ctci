from unittest import TestCase, main, skip

from ctci.datastructures.linkedlist import Node, LinkedList
from ctci.ch2.question1 import remove_dups, remove_dups_ii
from ctci.ch2.question2 import kth_to_last, kth_to_last_ii
from ctci.ch2.question3 import delete_middle_node
from ctci.ch2.question4 import partition
from ctci.ch2.question5 import sum_lists
from ctci.ch2.question6 import palindrome, palindrome_ii
from ctci.ch2.question7 import intersection
from ctci.ch2.question8 import loop_detection

class TestChapter2(TestCase):

    def test_remove_dups(self):
        test = LinkedList()
        test.add_list([1, 1, 1])

        remove_dups(test.head)
        self.assertEqual(test.string(), '1')

        test2 = LinkedList()
        test2.add_list([1, 2, 3])

        remove_dups(test2.head)
        self.assertEqual(test2.string(), '1 2 3')

        test3 = LinkedList()
        test3.add_list([1, 2, 2, 3])

        remove_dups(test3.head)
        self.assertEqual(test3.string(), '1 2 3')


    def test_remove_dups_ii(self):
        test = LinkedList()
        test.add_list([1, 1, 1])

        remove_dups_ii(test.head)
        self.assertEqual(test.string(), '1')

        test2 = LinkedList()
        test2.add_list([1, 2, 3])

        remove_dups_ii(test2.head)
        self.assertEqual(test2.string(), '1 2 3')

        test3 = LinkedList()
        test3.add_list([1, 2, 2, 3])

        remove_dups_ii(test3.head)
        self.assertEqual(test3.string(), '1 2 3')


    def test_kth_to_last(self):
        test = LinkedList()
        test.add_list([1, 2, 3, 4])

        self.assertEqual(kth_to_last(test.head, 1), 4)
        self.assertEqual(kth_to_last(test.head, 2), 3)
        self.assertEqual(kth_to_last(test.head, 3), 2)
        self.assertEqual(kth_to_last(test.head, 4), 1)


    def test_kth_to_last_ii(self):
        test = LinkedList()
        test.add_list([1, 2, 3, 4])

        self.assertEqual(kth_to_last_ii(test.head, 1), 4)
        self.assertEqual(kth_to_last_ii(test.head, 2), 3)
        self.assertEqual(kth_to_last_ii(test.head, 3), 2)
        self.assertEqual(kth_to_last_ii(test.head, 4), 1)


    def test_delete_middle_node(self):
        test = LinkedList()
        test.add_list(['a', 'b', 'c', 'd', 'e', 'f'])

        node = test.head.next.next
        delete_middle_node(node)

        self.assertEqual(test.string(), 'a b d e f')


    def test_partition(self):
        test = LinkedList()
        test.add_list([3, 5, 8, 5, 10, 2, 1])

        x = 5
        partition(test, x)

        curr = test.head
        while curr:
            if curr.data < 5 and curr.next:
                self.assertTrue(curr.data < curr.next.data)
            curr = curr.next

        test2 = LinkedList()
        test2.add_list([1, 2, 3, 5])

        x = 5
        partition(test2, x)

        curr = test.head
        while curr:
            if curr.data < 5 and curr.next:
                self.assertTrue(curr.data < curr.next.data)
            curr = curr.next


    def test_sum_lists(self):
        num1 = LinkedList()
        num1.add_list([7, 1, 6])

        num2 = LinkedList()
        num2.add_list([5, 9, 2])

        actual = sum_lists(num1, num2)

        expected = LinkedList()
        expected.add_list([9, 1, 2])

        self.assertEqual(actual.string(), expected.string())


    def test_palindrome(self):
        test1 = LinkedList()
        test1.add_list([1, 2, 3, 3, 2, 1])
        self.assertTrue(palindrome(test1.head))

        test2 = LinkedList()
        test2.add_list([1, 2, 3, 4, 3, 2, 1])
        self.assertTrue(palindrome(test2.head))

        test3 = LinkedList()
        test3.add_list([0, 1, 2, 3, 2, 1])
        self.assertFalse(palindrome(test3.head))

        test4 = LinkedList()
        test4.add_list([1, 2, 3, 4, 5, 5, 3, 1, 2])
        self.assertFalse(palindrome(test4.head))

        test5 = LinkedList()
        test5.add_list([1, 1])
        self.assertTrue(palindrome(test5.head))


    def test_palindrome_ii(self):
        test1 = LinkedList()
        test1.add_list([1, 2, 3, 3, 2, 1])
        palindrome_ii(test1.head)

        test2 = LinkedList()
        test2.add_list([1, 2, 3, 4, 3, 2, 1])
        self.assertTrue(palindrome_ii(test2.head))

        test3 = LinkedList()
        test3.add_list([0, 1, 2, 3, 2, 1])
        self.assertFalse(palindrome_ii(test3.head))

        test4 = LinkedList()
        test4.add_list([1, 2, 3, 4, 5, 5, 3, 1, 2])
        self.assertFalse(palindrome_ii(test4.head))

        test5 = LinkedList()
        test5.add_list([1, 1])
        self.assertTrue(palindrome_ii(test5.head))


    def test_intersection(self):
        test1a = LinkedList()
        test1a.head = Node(1)
        test1a.head.next = Node(2)
        test1a.head.next.next = Node(3)
        test1a.head.next.next.next = Node(4)
        test1a.head.next.next.next.next = Node(5)

        test1b = LinkedList()
        test1b.head = Node(1)
        test1b.head.next = Node(2)
        test1b.head.next.next = Node(3)
        test1b.head.next.next.next = test1a.head.next.next.next
        test1b.head.next.next.next.next = test1a.head.next.next.next.next

        node = test1a.head.next.next.next
        self.assertIs(intersection(test1a.head, test1b.head), node)

        test2a = LinkedList()
        test2a.add_list([1, 2, 3, 4, 5])

        test2b = LinkedList()
        test2b.add_list([1, 2, 3, 4, 5])
        self.assertIsNone(intersection(test2a.head, test2b.head))

        test3a = LinkedList()
        test3a.head = Node(1)
        test3a.head.next = Node(2)
        test3a.head.next.next = Node(3)
        test3a.head.next.next.next = Node(4)
        test3a.head.next.next.next.next = Node(5)

        test3b = LinkedList()
        test3b.head = Node(1)
        test3b.head.next = Node(2)
        test3b.head.next.next = test3a.head.next.next.next
        test3b.head.next.next.next = test3a.head.next.next.next.next

        node = test3a.head.next.next.next
        self.assertIs(intersection(test3a.head, test3b.head), node)


    def test_loop_detection(self):
        test1 = LinkedList()
        test1.head = Node(1)
        test1.head.next = Node(2)
        test1.head.next.next = Node(3)
        test1.head.next.next.next = Node(4)
        test1.head.next.next.next.next = test1.head.next.next

        node = test1.head.next.next
        self.assertIs(loop_detection(test1.head), node)

        test2 = LinkedList()
        test2.add_list([1, 2, 3, 4, 5])

        self.assertIsNone(loop_detection(test2.head))
