import string


# helper states table:
#
#       |  abcdef...  |   (   |    )    |    ~     |     | &
# ------|-------------|-------|---------|----------|----------------------
#   q0  |   q1, ->    |  +1   |   -1    |  q0, ->  |      qn
# ------|-------------|-------|---------|----------|----------------------
#   q1  |   qn        |  +1   |   -1    |  qn      |     q0, ->

class LogicExprChecker:

    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")
        self.current_state = 'q0'
        self.bracket_counter = 0

    def __call__(self): # mało intuicyjny iterfejs
        if len(self.expression) == 0:
            return False
        for x in self.expression:
            state = self.current_state
            self.move(x)
            print(f'{state}, {x} => {self.current_state}')  # gives info about steps
            if self.current_state == 'qn' or self.bracket_counter < 0:
                return False
        if self.current_state == 'q1' and self.bracket_counter == 0:
            return True
        return False

    def move(self, x):
        if self.current_state == 'q0':
            self.q0_step(x)
        elif self.current_state == 'q1':
            self.q1_step(x)

    def q0_step(self, x):
        if x in string.ascii_lowercase or x in string.digits:
            self.current_state = 'q1'
        elif x == '~':
            pass
        elif x == '(':
            self.bracket_counter += 1
        else:
            self.current_state = 'qn'  # q no -> rejecting state
            self.print_err_msg(x)

    def q1_step(self, x):
        if x in '&|':
            self.current_state = 'q0'
        elif x == ')':
            self.bracket_counter -= 1
        else:
            self.current_state = 'qn'
            self.print_err_msg(x)

    def print_err_msg(self, wrong_arg):
        print(f'Logical expression {self.expression} failed on argument: {wrong_arg}')
