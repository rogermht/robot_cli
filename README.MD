# Robot Challenge
Robot that take a MOVE, PLACE x y DIRECTION, LEFT and RIGHT commands

# Assumption
  - The user will issue the correct direction commands i.e. NORTH/SOUTH/WEST/EAST

# Installation
   - pip install -r requirements.txt
   - python setup.py install
# Running the program
   -  python robot_cli.py
# Examples of CLI
    Enter your robot command (press q to quit):
    >place 1 2 north
    >report
    The coordinate of the robot is (1, 2) and facing NORTH
    >move
    >report
    The coordinate of the robot is (1, 3) and facing NORTH
    >left
    >report
    The coordinate of the robot is (1, 3) and facing WEST
    >place 4 4 east
    >report
    The coordinate of the robot is (4, 4) and facing EAST
    >right
    >report
    The coordinate of the robot is (4, 4) and facing SOUTH
    >