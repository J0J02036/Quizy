# DISCLAIMER THIS IS MY CODING DONE MY WAY NOT YOURS DEAL WITH IT
import random
import sys
questions = []
answers_list = []
user_answer_list = []
number_of_restarts = 0


def time():
    import time

    t = time.localtime(time.time())  # tells you the time
    time_str = "Current Time:" + time.asctime(t)

    print(time_str)


def yes_no(question):  # checks for yes no response
    while True:
        want_instructions = input(question).lower()

        if want_instructions == "yes" or want_instructions == "y":
            return "yes"
        elif want_instructions == "no" or want_instructions == "n":
            return "no"
        else:
            print("you did not insert a valid response")


def num_check(question, low, high):  # checks the number (for levels)
    valid = False
    while not valid:

        error = f"please enter an integer that is at least {low} and less than {high}---"

        # ask for a number
        response_num_check = int(input(question))

        # check number is more than 0
        if response_num_check == "infinite":
            return "infinite"

        try:
            if low < response_num_check:
                return response_num_check

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


def float_check():  # checks user answer is a number
    valid = False
    while not valid:

        error = "please enter a number."

        try:
            response_num_check = input()
            # ask for a number
            response_num_check = float(response_num_check)

            # check number is more than 0

            return response_num_check

            # outputs error if input is invalid

        except ValueError:
            print(error)
            print()


'''
def difficulty_checker():
    response_function = int(input("Pick a level"))
    if response_function == 1:
        return response_function
    elif response_function == 2:
        return response_function
    elif response_function == 3:
        return response_function    #dunno out of use
    elif response_function == 4:
        return response_function
    else:
        print("plz enter a correct difficulty")
    return print("starting level", response_function)
'''


def level_1():  # level 1 settings
    while True:
        table_1 = random.randint(1, 4)
        first = random.randint(1, 10)
        second = random.randint(1, 10)

        if table_1 == 1:
            division_answer = first / second
            print(f"What is {first} / {second}?")
            func_table_answer = round(division_answer, 2)

            # adds question to list
            questions_func = first, "/", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 2:
            func_table_answer = first * second
            print(f"What is {first} X {second}?")

            # adds question to list
            questions_func = first, "X", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 3:
            func_table_answer = first + second
            print(f"What is {first} + {second}?")

            # adds question to list
            questions_func = first, "+", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 4:
            func_table_answer = first - second
            print(f"What is {first} - {second}?")

            # adds question to list
            questions_func = first, "-", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        else:
            print("error something has gone wrong with the program")


def start_l_1():  # def to start level 1
    correct_answers = 0
    number_of_rounds_done = 0
    sneakey = num_check("how many rounds", 1, "infinite")
    total_rounds = sneakey
    if total_rounds == "infinite":
        "infinite" == 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    else:
        pass

    while True:

        if number_of_rounds_done == 0:
            game_his_L.append("")
        game_his_L.append(f"question {number_of_rounds_done + 1}: ")
        level_1_answer = level_1()
        if debug == "yes":
            print("psst answer", level_1_answer)
        else:
            pass
        user_answer = float_check()

        game_his_L.append("You choose")
        game_his_L.append(user_answer)
        game_his_L.append("the correct answer is")
        game_his_L.append(level_1_answer)
        game_his_L.append("")
        game_his_L.append("")

        user_answer_list.append(user_answer)
        answers_list.append(level_1_answer)
        if user_answer == level_1_answer:  # todo int conversion is dangerous (use a try/except to protect your code)
            print("correct")
            correct_answers = correct_answers + 1
            number_of_rounds_done = number_of_rounds_done + 1
            print(number_of_rounds_done, "out of", total_rounds)

        else:
            print("incorrect")
            print("heads up this ones the correct one", level_1_answer)
            number_of_rounds_done = number_of_rounds_done + 1
            questions.append(number_of_rounds_done)
            print(number_of_rounds_done, "out of", total_rounds)
        if total_rounds == number_of_rounds_done:

            want_game_his = yes_no("do you want game history")
            print(f"you said {want_game_his} to seeing the history")
            if want_game_his == "yes":

                for item in game_his_L:
                    print(item)
            else:
                pass

            play_again = yes_no("do you want to play again")
            if play_again == "yes":
                print(number_of_restarts)
                return
            else:
                pass
            print("bye")
            quit()
        else:
            pass


def level_2():  # level 2 settings
    while True:
        table_1 = random.randint(1, 4)
        first = random.randint(1, 20)
        second = random.randint(1, 20)

        if table_1 == 1:
            division_answer = first / second
            print(f"What is {first} / {second}?")
            func_table_answer = round(division_answer, 2)

            # adds question to list
            questions_func = first, "/", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 2:
            func_table_answer = first * second
            print(f"What is {first} X {second}?")

            # adds question to list
            questions_func = first, "X", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 3:
            func_table_answer = first + second
            print(f"What is {first} + {second}?")

            # adds question to list
            questions_func = first, "+", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 4:
            func_table_answer = first - second
            print(f"What is {first} - {second}?")

            # adds question to list
            questions_func = first, "-", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        else:
            print("error something has gone wrong with the program")


def start_l_2():  # def to start level 2
    correct_answers = 0
    number_of_rounds_done = 0

    total_rounds = num_check("how many rounds", 1, "infinite")

    while True:

        if number_of_rounds_done == 0:
            game_his_L.append("")
        game_his_L.append(f"question {number_of_rounds_done + 1}: ")
        level_1_answer = level_2()
        if debug == "yes":
            print("psst answer", level_1_answer)
        else:
            pass
        user_answer = float_check()

        game_his_L.append("You choose")
        game_his_L.append(user_answer)
        game_his_L.append("the correct answer is")
        game_his_L.append(level_1_answer)
        game_his_L.append("")
        game_his_L.append("")

        user_answer_list.append(user_answer)
        answers_list.append(level_1_answer)
        if user_answer == level_1_answer:  # todo int conversion is dangerous (use a try/except to protect your code)
            print("correct")
            correct_answers = correct_answers + 1
            number_of_rounds_done = number_of_rounds_done + 1
            print(number_of_rounds_done, "out of", total_rounds)

        else:
            print("incorrect")
            print("heads up this ones the correct one", level_1_answer)
            number_of_rounds_done = number_of_rounds_done + 1
            questions.append(number_of_rounds_done)
            print(number_of_rounds_done, "out of", total_rounds)
        if total_rounds == number_of_rounds_done:

            want_game_his = yes_no("do you want game history")
            print(f"you said {want_game_his} to seeing the history")
            if want_game_his == "yes":

                for item in game_his_L:
                    print(item)
            else:
                pass

            play_again = yes_no("do you want to play again")
            if play_again == "yes":
                print(number_of_restarts)
                return
            else:
                pass
            print("bye")
            quit()
        else:
            pass


def level_3():  # level 3 settings
    while True:
        table_1 = random.randint(1, 4)
        first = random.randint(1, 100)
        second = random.randint(1, 100)

        if table_1 == 1:
            division_answer = first / second
            print(f"What is {first} / {second}?")
            func_table_answer = round(division_answer, 2)

            # adds question to list
            questions_func = first, "/", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 2:
            func_table_answer = first * second
            print(f"What is {first} X {second}?")

            # adds question to list
            questions_func = first, "X", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 3:
            func_table_answer = first + second
            print(f"What is {first} + {second}?")

            # adds question to list
            questions_func = first, "+", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 4:
            func_table_answer = first - second
            print(f"What is {first} - {second}?")

            # adds question to list
            questions_func = first, "-", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        else:
            print("error something has gone wrong with the program")


def start_l_3():  # def to start level 3
    correct_answers = 0
    number_of_rounds_done = 0

    total_rounds = num_check("how many rounds", 1, "infinite")

    while True:

        if number_of_rounds_done == 0:
            game_his_L.append("")
        game_his_L.append(f"question {number_of_rounds_done + 1}: ")
        level_1_answer = level_3()
        if debug == "yes":
            print("psst answer", level_1_answer)
        else:
            pass
        user_answer = float_check()

        game_his_L.append("You choose")
        game_his_L.append(user_answer)
        game_his_L.append("the correct answer is")
        game_his_L.append(level_1_answer)
        game_his_L.append("")
        game_his_L.append("")

        user_answer_list.append(user_answer)
        answers_list.append(level_1_answer)
        if user_answer == level_1_answer:  # todo int conversion is dangerous (use a try/except to protect your code)
            print("correct")
            correct_answers = correct_answers + 1
            number_of_rounds_done = number_of_rounds_done + 1
            print(number_of_rounds_done, "out of", total_rounds)

        else:
            print("incorrect")
            print("heads up this ones the correct one", level_1_answer)
            number_of_rounds_done = number_of_rounds_done + 1
            questions.append(number_of_rounds_done)
            print(number_of_rounds_done, "out of", total_rounds)
        if total_rounds == number_of_rounds_done:

            want_game_his = yes_no("do you want game history")
            print(f"you said {want_game_his} to seeing the history")
            if want_game_his == "yes":

                for item in game_his_L:
                    print(item)
            else:
                pass

            play_again = yes_no("do you want to play again")
            if play_again == "yes":
                print(number_of_restarts)
                return
            else:
                pass
            print("bye")
            quit()
        else:
            pass


def level_4():  # level 4 settings
    while True:
        table_1 = random.randint(1, 4)
        first = random.randint(1, 1000)
        second = random.randint(1, 1000)

        if table_1 == 1:
            division_answer = first / second
            print(f"What is {first} / {second}?")
            func_table_answer = round(division_answer, 2)

            # adds question to list
            questions_func = first, "/", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 2:
            func_table_answer = first * second
            print(f"What is {first} X {second}?")

            # adds question to list
            questions_func = first, "X", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 3:
            func_table_answer = first + second
            print(f"What is {first} + {second}?")

            # adds question to list
            questions_func = first, "+", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        elif table_1 == 4:
            func_table_answer = first - second
            print(f"What is {first} - {second}?")

            # adds question to list
            questions_func = first, "-", second
            questions.append(questions_func)

            game_his_L.append(f"{questions_func[0]} {questions_func[1]} {questions_func[2]} = ?")

            return func_table_answer
        else:
            print("error something has gone wrong with the program")


def start_l_4():  # def to start level 4
    correct_answers = 0
    number_of_rounds_done = 0

    total_rounds = num_check("how many rounds", 1, "infinite")

    while True:

        if number_of_rounds_done == 0:
            game_his_L.append("")
        game_his_L.append(f"question {number_of_rounds_done + 1}: ")
        level_1_answer = level_4()
        if debug == "yes":
            print("psst answer", level_1_answer)
        else:
            pass
        user_answer = float_check()

        game_his_L.append("You choose")
        game_his_L.append(user_answer)
        game_his_L.append("the correct answer is")
        game_his_L.append(level_1_answer)
        game_his_L.append("")
        game_his_L.append("")

        user_answer_list.append(user_answer)
        answers_list.append(level_1_answer)
        if user_answer == level_1_answer:  # todo int conversion is dangerous (use a try/except to protect your code)
            print("correct")
            correct_answers = correct_answers + 1
            number_of_rounds_done = number_of_rounds_done + 1
            print(number_of_rounds_done, "out of", total_rounds)

        else:
            print("incorrect")
            print("heads up this ones the correct one", level_1_answer)
            number_of_rounds_done = number_of_rounds_done + 1
            questions.append(number_of_rounds_done)
            print(number_of_rounds_done, "out of", total_rounds)
        if total_rounds == number_of_rounds_done:

            want_game_his = yes_no("do you want game history")
            print(f"you said {want_game_his} to seeing the history")
            if want_game_his == "yes":

                for item in game_his_L:
                    print(item)
            else:
                pass

            play_again = yes_no("do you want to play again")
            if play_again == "yes":
                print(number_of_restarts)
                return
            else:
                pass
            print("bye")
            quit()
        else:
            pass

def run_game():  # def to run/restart quiz
    print("pick a level")
    print('''L,1 = 1
    L,2 = 2
    l,3 = 3
    L,impossible = 4''')

    response = num_check("Pick a level", 0, 5)
    if response == 1:
        start_l_1()
    elif response == 2:
        start_l_2()
    elif response == 3:
        start_l_3()
    elif response == 4:
        start_l_4()
    elif response == 2810200869:  # secret level because why not "not done
        # start_the_secret_level() # secret level
        print("not yet buddy")  # tells you not complete yet
    else:
        print("plz enter a correct difficulty")
    # print("starting level", response)


# sets the amount of times played and changes text when you
# play/restart the round, so you don't get the welcome when you reset.
while True:

    number_of_restarts = number_of_restarts + 1
    if number_of_restarts == 1:
        print("welcome to my math quiz")
        print("this quiz is set up to round to 2 decimal places for example 1.'25' ")
        print("do not round to one or 3 or you will be wrong")
    else:
        print("play again lets see how much yoy get this time ;)")
        print("remember round to 2 decimal places for example 1.'25' ")
    test_pizza = yes_no("do you want to run debug mode?")
    debug = test_pizza
    time()
    game_his_L = []
    run_game()
