from src.table import Table


class Robot:
    '''
     Robot class that contains robot instance state and related behaviours. The behaviour of the robot will change according
     the current state.
    '''
    def __init__(self):
        '''
        Initialize instance states
        '''
        self._is_on_table = False
        self._x = None
        self._y = None
        self._direction = None

    def place(self, x, y, direction):
        '''
        Place command
        '''
        if not Table.is_within_boundary(int(x), int(y)):
            return
        if not self._is_on_table:
            self._is_on_table = True

        self._x = int(x)
        self._y = int(y)
        self._direction = direction.upper()

    def move(self, unit=1):
        '''
        Move command
        '''
        if self._is_on_table:
            x_y_vec = Table.calc_x_y_vec(self._direction)
            new_x = self._x + x_y_vec[0]*unit
            new_y = self._y + x_y_vec[1]*unit
            if not Table.is_within_boundary(new_x, new_y):
                # Ignore movement if move outside boundary of the table
                return
            self._x = new_x
            self._y = new_y

    def left(self):
        '''
        Turn left command
        '''
        if self._is_on_table:
            self._direction = Table.calc_left_transition(self._direction)

    def right(self):
        '''
        Turn right command
        '''
        if self._is_on_table:
            self._direction = Table.calc_right_transition(self._direction)

    def report(self):
        '''
        Report the robot x y ccordinate and direction
        '''
        return self._x, self._y, self._direction
