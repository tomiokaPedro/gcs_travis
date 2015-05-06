import unittest
from sort_list import sort_list, bubbleSort

class TestSortList(unittest.TestCase):



    def setUp(self):
        self.unsorted_array = [3,5,6,1,2,9,8,7,4]
        self.expected_array = [1,2,3,4,5,6,7,8,9]

    def testSortOrder(self):

        sorted_array = sort_list(self.unsorted_array)

        self.assertEqual(self.expected_array, sorted_array)


    def tearDown(self):
        pass

    def testBubbleSort(self):
        sorted_array = bubbleSort(self.unsorted_array)

        self.assertEqual(self.expected_array, sorted_array)


if __name__ == "__main__":
    unittest.main()

