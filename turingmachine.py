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
        if self.question_number == 1:
            self.alphabet = ['1', '#', '0']
        if self.question_number == 2:
            self.alphabet = ['a', '#', 'b']
        if self.question_number == 3 or self.question_number == 4:
            self.alphabet = ['a', 'b', 'c']
        for i in input_list:
            if i not in self.alphabet:
                print(f"Error: character {i} in input not in the alphabet")
                sys.exit()
        self.state = 'q0'
        self.head = 0
        self.tape = input_list
        self.tape.append(blank)
        print(self.tape)

    def transFuncQ1(self):

        ## check if input is valid
        if self.state == "q0":
            if self.tape[self.head] == "1":
                # self.tape[self.head] = "X"
                self.move_head_right()
                self.state = "q1"
            else:
                print(f"q0 = Input is rejected")
                sys.exit()

        elif self.state == "q1":
            if self.tape[self.head] == "1":
                # self.tape[self.head] = "X"
                self.move_head_right()
            elif self.tape[self.head] == "#":
                self.move_head_right()
                self.state = "q2"
            else:
                print(f"q1 = Input is rejected")
                sys.exit()

        elif self.state == "q2":
            if self.tape[self.head] == "0":
                self.move_head_right()
            elif self.tape[self.head] == " ":
                self.move_head_left()
                if (self.tape[self.head] == "0"):
                    self.tape[self.head] = "B"
                    self.move_head_left()
                    self.state = "q3"
            else:
                print(f"q2 = Input is rejected")
                sys.exit()

        ## starting from q3 we check the sum of left and right sides

        elif self.state == "q3":
            if self.tape[self.head] == "0":
                self.move_head_left()
            elif self.tape[self.head] == "#":
                self.move_head_left()
            elif self.tape[self.head] == "1":
                self.tape[self.head] = "X"
                self.move_head_left()
                self.state = "q3.1"
            else:
                print(f"q3 = Input is rejected")
                sys.exit()

        elif self.state == "q3.1":
            if self.tape[self.head] == "1":
                self.tape[self.head] = "X"
                self.move_head_right()
            elif self.tape[self.head] == "0":
                self.move_head_right()
            elif self.tape[self.head] == "X":
                self.move_head_right()
            elif self.tape[self.head] == "#":
                self.move_head_right()
            elif self.tape[self.head] == "B":
                self.move_head_left()
                self.state = "q4"
            else:
                print(f"q3.1 = Input is rejected")
                sys.exit()

        # this blocks will repeate
        elif self.state == "q4":
            if self.tape[self.head] == "0":
                self.tape[self.head] = "B"
                self.move_head_left()
                self.state = "q4.1"
                # self.state = "q5"
            elif self.tape[self.head] == "#":
                self.move_head_left()
                self.state = "end"
            else:
                self.move_head_left()
                self.state = "end"
                # print(f"q4 = Input is rejected")
                # sys.exit()


        elif self.state == "q4.1":
            if self.tape[self.head] == "0":
                self.move_head_left()
            elif self.tape[self.head] == "#":
                self.move_head_left()
                self.state = "q5"
            else:
                print(f"q4.1 = Input is rejected")
                sys.exit()

        elif self.state == "q5":
            # if self.tape[self.head] == "0":
            #     self.move_head_left()
            if self.tape[self.head] == "#":
                self.move_head_left()
                self.state = "q5.2"
            elif self.tape[self.head] == "Y":
                self.move_head_right()
            elif self.tape[self.head] == "X":
                self.tape[self.head] = "Y"
                self.move_head_left()
                self.state = "q5.1"
            elif self.tape[self.head] == "1" or self.tape[self.head] == " ":
                self.move_head_right()
                self.state = "q5.2"
            else:
                print(f"q5 = Input is rejected")
                sys.exit()

        elif self.state == "q5.1":
            if self.tape[self.head] == "1":
                self.tape[self.head] = "Y"
                self.move_head_right()
                self.state = "q5"
            elif self.tape[self.head] == "X":
                self.move_head_left()
            elif self.tape[self.head] == "Y":
                self.move_head_left()
            elif self.tape[self.head] == " ":
                self.move_head_right()
                self.state = "q5.3"
            else:
                print(f"q5.1 = Input is rejected")
                sys.exit()


        ## change all Y to X
        elif self.state == "q5.2":
            if self.tape[self.head] == "Y":
                self.tape[self.head] = "X"
                self.move_head_left()
            elif self.tape[self.head] == "B":
                self.move_head_left()
                self.state = "q4"
            else:
                self.move_head_right()


        elif self.state == "q5.3":
            if self.tape[self.head] == "#":
                self.move_head_left()
                self.state = "end"
            else:
                print(f"q5.3 = Input is rejected")
                sys.exit()

        elif self.state == "end":
            if self.tape[self.head] == "X":
                self.move_head_left()
            elif self.tape[self.head] == " ":
                self.accepted = True
                print(f"Input is accepted on state end")
            else:
                print(f"End function: Input is rejected")
                sys.exit()

        # elif self.state == "back_to_hash":
        #     if self.tape[self.head] == "X":
        #         self.move_head_left()
        #     elif self.tape[self.head] == "#":
        #         self.move_head_left()
        #         self.state = "back_to_start"
        #     else:
        #         print(f"Input is rejected")
        #         sys.exit()

        # elif self.state == "back_to_start":
        #     if self.tape[self.head] == "X":
        #         self.move_head_left()
        #     elif self.tape[self.head] == " ":
        #         self.move_head_right()
        #         self.state = "start"
        #     else:
        #         print(f"Input is rejected")
        #         sys.exit()
        # Настин код здесь :)

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
                self.move_head_right()
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
                    self.tape[self.head] == 'c' or \
                    self.tape[self.head] == 'Y' or \
                    self.tape[self.head] == 'Z':
                self.move_head_left()
            elif self.tape[self.head] == 'X':
                self.move_head_right()
                self.state = 'q0'
            elif self.tape[self.head] == blank:
                self.move_head_left()
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

    def transFuncQ4(self):
        if self.state == 'q0':
            if self.tape[self.head] == 'a':
                self.tape[self.head] = 'X'
                self.move_head_right()
                self.state = 'q1'
            elif self.tape[self.head] == 'b':
                self.move_head_right()
                self.state = 'q5'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q1':
            if self.tape[self.head] == 'a':
                self.move_head_right()
            elif self.tape[self.head] == 'b':
                self.tape[self.head] = 'Y'
                self.move_head_right()
                self.state = 'q2'
            elif self.tape[self.head] == 'Z':
                self.move_head_left()
                self.state = 'q4'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q2':
            if self.tape[self.head] == 'b' or self.tape[self.head] == 'Z':
                self.move_head_right()
            elif self.tape[self.head] == 'c':
                self.tape[self.head] = 'Z'
                self.move_head_left()
                self.state = 'q3'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q3':
            if self.tape[self.head] == 'b' or self.tape[self.head] == 'Z':
                self.move_head_left()
            elif self.tape[self.head] == 'Y':
                self.move_head_right()
                self.state = 'q1'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q4':
            if self.tape[self.head] == 'a':
                self.move_head_left()
            elif self.tape[self.head] == 'Y':
                self.tape[self.head] = 'b'
                self.move_head_left()
            elif self.tape[self.head] == 'X':
                self.move_head_right()
                self.state = 'q0'
            else:
                print(f"Input is rejected")
                sys.exit()

        elif self.state == 'q5':
            if self.tape[self.head] == 'Z' or self.tape[self.head] == 'b':
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
        elif self.question_number == 4:
            self.setup()
            while not self.accepted:
                self.transFuncQ4()
        elif self.question_number == 1:
            self.setup()
            while not self.accepted:
                self.transFuncQ1()


turmach = TuringMachine(1, '1111111111111111#0000')

turmach.run()