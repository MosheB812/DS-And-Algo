from challenges import A_Lists
import unittest

# Test Cases for all List Challenges


class tstLists(unittest.TestCase):
    # Challenge 1: Remove Even Integers from List
    def test_add_LstRemoveEven1(self):
        actual = A_Lists.remove_even([1, 2, 4, 5, 10, 6, 3])
        expected = [1, 5, 3]
        self.assertEqual(actual, expected)

    def test_add_LstRemoveEven2(self):
        actual = A_Lists.remove_even([14, -100, 166, -2, -167, 20, 30, -38, 43, -194, 114,  182, 38, -85, -152, 111,
                                      109, -104, -32, -133, 62, -128, -6, -69, -46, 4, -102, -41, -122, -174, 26, -43, -154, -172, 69, 93, -9])
        expected = [-167, 43, -85, 111, 109, -133, -69, -41, -43, 69, 93, -9]
        self.assertEqual(actual, expected)

    # Challenge 2: Merge Two Sorted Lists
    def test_add_merge_lists1(self):
        actual = A_Lists.merge_lists([1, 3, 4, 5], [2, 6, 7, 8])
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(actual, expected)

    def test_add_merge_lists2(self):
        actual = A_Lists.merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_add_merge_lists3(self):
        actual = A_Lists.merge_lists([], [1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_add_merge_lists4(self):
        actual = A_Lists.merge_lists([1, 4, 45, 63], [])
        expected = [1, 4, 45, 63]
        self.assertEqual(actual, expected)

    def test_add_merge_lists5(self):
        actual = A_Lists.merge_lists(
            [4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4])
        expected = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.assertEqual(actual, expected)

    def test_add_merge_lists6(self):
        actual = A_Lists.merge_lists([-133, -100, 0, 4], [-2000, 2000])
        expected = [-2000, -133, -100, 0, 4, 2000]
        self.assertEqual(actual, expected)

    # Challenge 3: Find Two Numbers that Add up to "k"
    def test_add_findSum1(self):
        actual = A_Lists.find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81)
        expected = [21, 60]
        self.assertEqual(actual, expected)

    # Challenge 4: List of Products of all Elements
    def test_add_find_product1(self):
        actual = A_Lists.find_product([1, 2, 3, 4])
        expected = [24, 12, 8, 6]
        self.assertEqual(actual, expected)

    def test_add_find_product2(self):
        actual = A_Lists.find_product([2, 5, 9, 3, 6])
        expected = [810, 324, 180, 540, 270]
        self.assertEqual(actual, expected)

    def test_add_find_product3(self):
        actual = A_Lists.find_product([0, 1, 10, 100])
        expected = [1000, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_add_find_product4(self):
        actual = A_Lists.find_product([0, 2, 9, 0, 12, 25])
        expected = [0, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    # Challenge 5: Find Minimum Value in List
    def test_add_find_minimum1(self):
        actual = A_Lists.find_minimum([100, 12, 34, 40])
        expected = 12
        self.assertEqual(actual, expected)

    def test_add_find_minimum2(self):
        actual = A_Lists.find_minimum([4, 5, 0, 3, 6])
        expected = 0
        self.assertEqual(actual, expected)

    # Challenge 7: Find Second Max Value in a List
    def test_add_find_second_maximum1(self):
        actual = A_Lists.find_second_maximum([9, 2, 3, 6])
        expected = 6
        self.assertEqual(actual, expected)

    def test_add_find_second_maximum2(self):
        actual = A_Lists.find_second_maximum([4, 2, 1, 5, 0])
        expected = 4
        self.assertEqual(actual, expected)

    # Challenge 8: Right Rotate List
    def test_add_right_rotate1(self):
        actual = A_Lists.right_rotate([], 1)
        expected = []
        self.assertEqual(actual, expected)

    def test_add_right_rotate2(self):
        actual = A_Lists.right_rotate([1, 2, 3, 4, 5], 2)
        expected = [4, 5, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_add_right_rotate3(self):
        actual = A_Lists.right_rotate([300, -1, 3, 0], 3)
        expected = [-1, 3, 0, 300]
        self.assertEqual(actual, expected)

    def test_add_right_rotate4(self):
        actual = A_Lists.right_rotate([0, 0, 0, 2], 2)
        expected = [0, 2, 0, 0]
        self.assertEqual(actual, expected)

    def test_add_right_rotate5(self):
        actual = A_Lists.right_rotate(['13', 'a', 'Python'], 3)
        expected = ['13', 'a', 'Python']
        self.assertEqual(actual, expected)

    def test_add_right_rotate6(self):
        actual = A_Lists.right_rotate(['right', 'rotate', 'python'], 4)
        expected = ['python', 'right', 'rotate']
        self.assertEqual(actual, expected)

    # def test_add_(self):
    #     actual =
    #     expected =
    #     self.assertEqual(actual, expected)
