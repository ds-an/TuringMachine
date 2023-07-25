import sys

blank = ' '

class TuringMachine:
    def __init__(self, question_number, input_str):
        self.state = ''
        self.head = None
        self.tape = []
        self.alphabet = []
        self.accepted = False
        self.input_str = input_str
        self.question_number = question_number

    def move_head_right(self):
        self.head += 1

    def move_head_left(self):
        self.head -= 1

    def setup(self):
        self.accepted = False
        input_list = list(self.input_str)
        if self.question_number == 2:
            self.alphabet = ['a', '#', 'b']
        if self.question_number == 3:
            self.alphabet = ['a', 'b', 'c']
        for i in input_list:
            if i not in self.alphabet:
                print(f"Error: character {i} in input not in the alphabet"
                      f" for Q2")
                sys.exit()
        self.state = 'q0'
        self.head = 0
        self.tape = input_list
        self.tape.append(blank)
        print(self.tape)

    def transFuncQ2(self):
        if self.state == 'q0':
            if self.tape[self.head] == '#':
                print(f"Input is rejected")
                sys.exit()
            else:
                self.state = 'q1'

        elif self.state == 'q1':
            if self.tape[self.head] == 'a':
                self.tape[self.head] = blank
                self.move_head_right()
                self.state = 'q1.5'
            elif self.tape[self.head] == 'b':
                self.tape[self.head] = blank
                self.move_head_right()
                self.state = 'q5'
            elif self.tape[self.head] == '#':
                self.state = 'qf'
                print(f"Input is accepted")
                self.accepted = True
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q1.5':
            if self.tape[self.head] == 'a' or self.tape[self.head] == 'b':
                self.move_head_right()
            elif self.tape[self.head] == '#':
                self.state = 'q2'
                self.move_head_right()
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q2':
            if self.tape[self.head] == 'a' or self.tape[self.head] == 'b':
                self.move_head_right()
            elif self.tape[self.head] == blank:
                self.move_head_left()
                self.state = 'q3'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q3':
            if self.tape[self.head] == 'a':
                self.tape[self.head] = blank
                self.move_head_left()
                self.state = 'q4'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q4':
            if self.tape[self.head] == 'a' or \
                    self.tape[self.head] == 'b' or \
                    self.tape[self.head] == '#':
                self.move_head_left()
            elif self.tape[self.head] == blank:
                self.move_head_right()
                self.state = 'q1'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q5':
            if self.tape[self.head] == 'a' or self.tape[self.head] == 'b':
                self.move_head_right()
            elif self.tape[self.head] == '#':
                self.state = 'q6'
                self.move_head_right()
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q6':
            if self.tape[self.head] == 'a' or self.tape[self.head] == 'b':
                self.move_head_right()
            elif self.tape[self.head] == blank:
                self.move_head_left()
                self.state = 'q7'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q7':
            if self.tape[self.head] == 'b':
                self.tape[self.head] = blank
                self.move_head_left()
                self.state = 'q8'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q8':
            if self.tape[self.head] == 'a' or \
                    self.tape[self.head] == 'b' or \
                    self.tape[self.head] == '#':
                self.move_head_left()
            elif self.tape[self.head] == blank:
                self.move_head_right()
                self.state = 'q1'
            else:
                print(f"Input is rejected")
                sys.exit()

    def transFuncQ3(self):
        if self.state == 'q0':
            if self.tape[self.head] == 'a':
                self.tape[self.head] = 'X'
                self.move_head_right()
                self.state = 'q1'
            elif self.tape[self.head] == 'Y':
                self.state = 'q4'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q1':
            if self.tape[self.head] == 'a':
                self.move_head_right()
            elif self.tape[self.head] == 'Y':
                self.move_head_right()
            elif self.tape[self.head] == 'b':
                self.tape[self.head] = 'Y'
                self.move_head_right()
                self.state = 'q2'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q2':
            if self.tape[self.head] == 'b':
                self.move_head_right()
            elif self.tape[self.head] == 'Z':
                self.move_head_right()
            elif self.tape[self.head] == 'c':
                self.tape[self.head] = 'Z'
                self.move_head_right()
                self.state = 'q3'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q3':
            if self.tape[self.head] == 'a' or \
                    self.tape[self.head] == 'b' or \
                    self.tape[self.head] == 'Y' or \
                    self.tape[self.head] == 'Z':
                self.move_head_left()
            elif self.tape[self.head] == 'X':
                self.move_head_right()
                self.state = 'q0'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q4':
            if self.tape[self.head] == 'Y' or \
                    self.tape[self.head] == 'Z':
                self.move_head_right()
            elif self.tape[self.head] == blank:
                self.state = 'qf'
                self.accepted = True
                print(f"The input is accepted")
            else:
                print(f"Input is rejected")
                sys.exit()

    def run(self):
        if self.question_number == 2:
            self.setup()
            while not self.accepted:
                self.transFuncQ2()
        elif self.question_number == 3:
            self.setup()
            while not self.accepted:
                self.transFuncQ3()


turmach = TuringMachine(3, 'aabbc')

turmach.run()
