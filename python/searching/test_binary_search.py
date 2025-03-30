import unittest

from python.searching.binary_search import find, NOT_FOUND


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.test_array = [-7, -5, -3, 0, 1, 2, 5, 9, 10, 13, 15, 21, 34, 45, 51, 53, 55]
        self.empty_array = []
        self.single_element_array = [1]

    def test_binary_search_found(self):
        # arrange
        key = self.test_array[13]
        expected_value = 13

        # act
        result = find(self.test_array, key)

        # assert
        self.assertEqual(expected_value, result)

    def test_binary_search_not_found(self):
        # arrange
        key = 7
        expected_value = NOT_FOUND

        # act
        result = find(self.test_array, key)

        # assert
        self.assertEqual(expected_value, result)

    def test_binary_search_first_element_found(self):
        # arrange
        key = self.test_array[0]
        expected_value = 0

        # act
        result = find(self.test_array, key)

        # assert
        self.assertEqual(expected_value, result)

    def test_binary_search_last_element_found(self):
        # arrange
        key = self.test_array[-1]
        expected_value = len(self.test_array) - 1

        # act
        result = find(self.test_array, key)

        # assert
        self.assertEqual(expected_value, result)

    def test_binary_search_empty_array(self):
        # arrange
        key = 45
        expected_value = NOT_FOUND

        # act
        result = find(self.empty_array, key)

        # assert
        self.assertEqual(expected_value, result)

    def test_binary_search_single_element_found(self):
        # arrange
        key = self.single_element_array[0]
        expected_value = 0

        # act
        result = find(self.single_element_array, key)

        # assert
        self.assertEqual(expected_value, result)

    def test_binary_search_single_element_not_found(self):
        # arrange
        key = 45
        expected_value = NOT_FOUND

        # act
        result = find(self.single_element_array, key)

        # assert
        self.assertEqual(expected_value, result)