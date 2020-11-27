from Figures import Circle, Rectangle, Triangle, Square
from Utils import *


class Program:
    FIGURES = {'circle': Circle, 'rectangle': Rectangle, 'triangle': Triangle, 'square': Square}
    ACTIONS = {'add', 'remove', 'move', 'scale', 'rotate', 'set border color', 'set background color', 'help', 'quit'}

    def __init__(self):
        self.figures = dict()

    def add_figure(self, figure, name, *size):
        name = validate_name(name)
        if name in self.figures.keys():
            raise ValueError(f'Name {name} name already exists.')
        if figure.lower() not in Program.FIGURES.keys():
            raise ValueError(f'Figure {figure} not available. Available figures: {self.FIGURES.values()}')

        self.figures[name] = Program.FIGURES[figure.lower()](name, *size)

    def remove_figure(self, name):
        name = check_name_exists(name, self.figures.keys())
        del self.figures[name]

    def quit(self):
        for figure in self.figures.values():
            print(figure)

    def help(self):
        print(f'''Available commands:
                    add <figure> <name> <size>
                    remove <name>
                    move <name> <vector>
                    scale <name> <ratio>
                    rotate <name> <angle>
                    set border color <name> <color>
                    set background color <name> <color>
                    help
                    quit

        <figure> is one of: circle, square, rectangle, triangle
        <name> - any unique identifier which may contain letters, numbers and underscores, not starting with a number 
        <ratio> - any real number other than 0
        <angle> - any angle in degrees
        <color> is one of: black, white, red, green, blue, cyan, magenta, yellow
        ''')

    def parse_command(self, command):
        parsed_command = command.lower().split()
        action = parsed_command[0]
        parameters = parsed_command[1:]
        if action == 'set':
            action = f'{parsed_command[0]} {parsed_command[1]} {parsed_command[2]}'
            parameters = parsed_command[3:]
        if action not in self.ACTIONS:
            raise ValueError(f'Action {action} is not available. Available actions: {self.ACTIONS}')
        return action, parameters

    def run(self):
        while 1:    # while True
            try:
                command = input('Type command: ')
                action, parameters = self.parse_command(command)
                if action == 'add':
                    self.add_figure(*parameters)
                elif action == 'remove':
                    self.remove_figure(*parameters)
                elif action == 'help':
                    self.help()
                elif action == 'quit':
                    self.quit()
                    break
                else:
                    self.run_figures(action, parameters)
            except (ValueError, IndexError, TypeError) as e:
                print(e)    # add_figure() missing 1 required positional argument: 'name' - mało czytelny komunikat

    def run_figures(self, action, parameters):  # nieczytelna nazwa
        name = check_name_exists(parameters[0], self.figures.keys())
        params = parameters[1:]
        if action == 'move':
            self.figures[name].move(*params)
        elif action == 'scale':
            self.figures[name].scale(*params)
        elif action == 'rotate':
            self.figures[name].rotate(*params)
        elif action == 'set border color':
            self.figures[name].set_border_color(*params)
        elif action == 'set background color':
            self.figures[name].set_background_color(*params)

