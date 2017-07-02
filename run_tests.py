from unittest import TextTestRunner, TestSuite, makeSuite

from ctci.tests.test_ch1 import TestChapter1

if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(makeSuite(TestChapter1))

    runner = TextTestRunner()
    runner.run(suite)
