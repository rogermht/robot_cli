# Author: Roger Ting
# Date:1/3/2019
# Description: Unit test the Table module


import unittest
from src.table import NORTH
from src.table import SOUTH
from src.table import EAST
from src.table import WEST
from src.table import Table


class TestTable(unittest.TestCase):

    def test_is_with_boundary(self):
        result = Table.is_within_boundary(5,5)
        self.assertEqual(False, result)
        result = Table.is_within_boundary(1, 4)
        self.assertEqual(True, result)

    def test_calc_x_y_vec(self):
        result = Table.calc_x_y_vec(NORTH)
        self.assertEqual((0,1), result)

    def test_calc_right_transition(self):
        result = Table.calc_right_transition(NORTH)
        self.assertEqual(EAST, result)

        result = Table.calc_right_transition(SOUTH)
        self.assertEqual(WEST, result)

    def test_calc_left_transition(self):
        result = Table.calc_left_transition(NORTH)
        self.assertEqual(WEST, result)

        result = Table.calc_left_transition(SOUTH)
        self.assertEqual(EAST, result)

if __name__ == '__main__':
    unittest.main()
