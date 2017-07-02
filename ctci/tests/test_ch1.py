from unittest import TestCase, main, skip

from ctci.ch1.question1 import is_unique
from ctci.ch1.question1 import is_unique_2
from ctci.ch1.question2 import check_permutation
from ctci.ch1.question3 import urlify
from ctci.ch1.question4 import palindrome_permutation
from ctci.ch1.question5 import one_away
from ctci.ch1.question6 import string_compression
from ctci.ch1.question7 import rotate_matrix
from ctci.ch1.question8 import zero_matrix
from ctci.ch1.question9 import string_rotation

class TestChapter1(TestCase):

    def test_is_unique(self):
        self.assertFalse(is_unique('hello'))
        self.assertTrue(is_unique('abc'))


    def test_is_unique_2(self):
        self.assertFalse(is_unique_2('hello'))
        self.assertTrue(is_unique('abc'))


    def test_check_permutation(self):
        self.assertTrue(check_permutation('abc', 'bca'))
        self.assertFalse(check_permutation('hello', 'world'))


    def test_urlify(self):
        urlify_input = 'Mr John Smith       '
        urlify_output = 'Mr%20John%20Smith'
        self.assertEqual(urlify(urlify_input), urlify_output)


    def test_palindrome_permutation(self):
        self.assertTrue(palindrome_permutation('Tact Coa'))


    def test_one_away(self):
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertFalse(one_away('pale', 'bake'))


    def test_string_compression(self):
        input1 = 'aabcccccaaa'
        output1 = 'a2b1c5a3'
        self.assertEqual(string_compression(input1), output1)

        input2 = 'a'
        output2 = 'a'
        self.assertEqual(string_compression(input2), output2)

        input3 = 'aaaaa'
        output3 = 'a5'
        self.assertEqual(string_compression(input3), output3)


    @skip
    def test_rotate_matrix(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                 [13, 14, 15, 16]]
        rotated = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3],
                  [16, 12, 8, 4]]

        rotate_matrix(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.assertEqual(matrix[i][j], rotated[i][j])


    def test_zero_matrix(self):
        matrix = [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 1, 2], [3, 4, 1, 2]]
        zeroed = [[0, 0, 0, 0], [4, 0, 6, 7], [8, 0, 1, 2], [3, 0, 1, 2]]

        zero_matrix(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.assertEqual(matrix[i][j], zeroed[i][j])


    def test_string_rotation(self):
        s1 = 'waterbottle'
        s2 = 'erbottlewat'
        self.assertTrue(string_rotation(s1, s2))

        s1 = 'helloworld'
        s2 = 'hi'
        self.assertFalse(string_rotation(s1, s2))


if __name__ == '__main__':
    main()
