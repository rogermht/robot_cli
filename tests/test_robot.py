# Author: Roger Ting
# Date:1/3/2019
# Description: Unit test the Robot module


import unittest
from src.robot import Robot
from src.table import NORTH
from src.table import SOUTH
from src.table import EAST
from src.table import WEST
from mock import patch


class TestRobot(unittest.TestCase):
    def test_no_initial_placement(self):
        test_robot = Robot()
        test_robot.move()
        result = test_robot.report()
        self.assertEqual((None, None, None), result)

    @patch('src.table.Table.is_within_boundary')
    def test_place(self, mock_is_within_boundary):
        mock_is_within_boundary.return_value = True
        test_robot = Robot()
        test_robot.place(1, 1, SOUTH)
        result = test_robot.report()
        self.assertEqual((1, 1, SOUTH), result)

    @patch('src.table.Table.is_within_boundary')
    @patch('src.table.Table.calc_x_y_vec')
    def test_move(self, mock_calc_x_y_vec, mock_is_within_boundary):
        mock_is_within_boundary.return_value = True
        mock_calc_x_y_vec.return_value = (0, 1)
        test_robot = Robot()
        test_robot.place(1, 1, NORTH)
        test_robot.move()
        result = test_robot.report()
        self.assertEqual((1, 2, NORTH), result)

    @patch('src.table.Table.is_within_boundary')
    @patch('src.table.Table.calc_left_transition')
    def test_left(self, mock_calc_left_transition, mock_is_within_boundary):
        mock_is_within_boundary.return_value = True
        mock_calc_left_transition.return_value = WEST
        test_robot = Robot()
        test_robot.place(1, 1, NORTH)
        test_robot.left()
        result = test_robot.report()
        self.assertEqual((1, 1, WEST), result)

    @patch('src.table.Table.is_within_boundary')
    @patch('src.table.Table.calc_left_transition')
    def test_right(self, mock_calc_right_transition, mock_is_within_boundary):
        mock_is_within_boundary.return_value = True
        mock_calc_right_transition.return_value = EAST
        test_robot = Robot()
        test_robot.place(1, 1, NORTH)
        test_robot.right()
        result = test_robot.report()
        self.assertEqual((1, 1, EAST), result)

    @patch('src.table.Table.is_within_boundary')
    @patch('src.table.Table.calc_x_y_vec')
    def test_boundary(self, mock_calc_x_y_vec, mock_is_within_boundary):
        mock_is_within_boundary.return_value = True
        mock_calc_x_y_vec.return_value = (0, 1)
        test_robot = Robot()
        test_robot.place(1, 4, NORTH)
        mock_is_within_boundary.return_value = False
        test_robot.move()
        result = test_robot.report()
        self.assertEqual((1, 4, NORTH), result)


if __name__ == '__main__':
    unittest.main()
