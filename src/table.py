_width = 5
_length = 5

NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

# Direction related structure can be expanded e.g North East
_DIRECTION_SET = {NORTH, EAST, SOUTH, WEST, }

_DIRECTION_TO_VEC_DICT = {
    NORTH: (0, 1),
    EAST: (1, 0),
    WEST: (-1, 0),
    SOUTH: (0, -1),
}

_LEFT_TRANSITION = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH,
}

_RIGHT_TRANSITION = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH,
}


class Table:
    '''
    All the table states and states transition logic reside here.
    Arguably, Singleton design pattern
    '''

    @staticmethod
    def is_within_boundary(x, y):
        '''
        Check whether x,y coordinate still within the boundary of the table
        '''
        return 0 <= x < _width and 0 <= y < _length

    @staticmethod
    def calc_x_y_vec(direction):
        '''
        Given a direction, return the x, y movement on the table
        '''
        return  _DIRECTION_TO_VEC_DICT[direction.upper()]

    @staticmethod
    def calc_left_transition(direction):
        '''
        Return the direction on the table given the object turn left
        '''
        return _LEFT_TRANSITION[direction.upper()]

    @staticmethod
    def calc_right_transition(direction):
        '''
          Return the direction on the table given the object turn right
        '''
        return _RIGHT_TRANSITION[direction.upper()]
