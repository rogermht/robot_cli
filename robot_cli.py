from src.robot import Robot
import shlex


def run_cli():
    cli_robot = Robot()
    print "Enter your robot command (press q to quit):"

    while True:
        shell_command = raw_input('>')
        shell_command = shell_command.strip().lower()
        if not shell_command:
            continue
        if shell_command == 'q':
            break

        words = shlex.split(shell_command)

        # Grab the arguments
        args = words[1:] if len(words) > 1 else []

        # Grab the method
        method_name = words[0]
        try:
            method = getattr(cli_robot, words[0])
            result = method(*args)
            if result:
                print "The coordinate of the robot is (%s, %s) and facing %s" % result
        except:
                print "Class {} does not implement {} command".format(cli_robot.__class__.__name__, method_name.upper())


if __name__ == '__main__':
    run_cli()
