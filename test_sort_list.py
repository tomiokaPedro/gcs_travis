import unittest
from sort_list import sort_list

class TestSortList(unittest.TestCase):

    def setUp(self):
        pass

    def testSortOrder(self):

        unsorted_array = [3,5,6,1,2,9,8,7,4]
        expected_array = [1,2,3,4,5,6,7,8,9]
    
        sorted_array = sort_list(unsorted_array)

        self.assertEqual(expected_array, sorted_array)


    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()

