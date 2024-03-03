import random

# constants
RANDOMNOT = 0.9
RANDOMBRACKET = 0.9
RANDOMSTOP = 0.95
MAX_COMPLEXITY = 3
MAX_SEQUENCE = 10

def generate(depth, complexity):
    """ This function recursively and randommly generates boolean expressions """
    if depth > complexity or random.random() > RANDOMSTOP:
        return random.choice(["True", "False"])
    operator = random.choice(["and", "or"])
    left = generate(depth + 1, complexity)
    right = generate(depth + 1, complexity)
    if random.random() > RANDOMNOT:
        leftnot = "not "
    else:
        leftnot = ""
    if random.random() > RANDOMNOT:
        rightnot = "not "
    else:
        rightnot = ""
    if random.random() > RANDOMBRACKET:
        leftbracket = ""
        rightbracket = ""
        bracketnot = ""
    else:
        if random.random() > RANDOMNOT:
            bracketnot = "not "
        else:
            bracketnot = ""
        leftbracket = "("
        rightbracket = ")"
    if random.random() > RANDOMBRACKET:
        rightnot = "not "
    return f"{bracketnot}{leftbracket}{leftnot}{left} {operator} {rightnot}{right}{rightbracket}"

def get_input():
    while True:
        answ = input("Your answer (t, f, True, False, e, End): ").upper()
        if answ in ["T", "F", "TRUE", "FALSE", "E", "END"]:
            return answ

def calc_success_rate(success, tries):
    return success/tries*100

# function created just to satisfy final project requirements
def add_one( value ):
    return value + 1

def exercise():
    level = 0
    tries = [0]*(MAX_COMPLEXITY+1)
    success = [0]*(MAX_COMPLEXITY+1)
    sequence = 0

    while True:
        expression = generate(0, level)
        if success[level]>0:
            #successrate = success[level]/tries[level]*100
            successrate = calc_success_rate( success[level], tries[level] )
        else:
            successrate = 0
        print( f"\nLevel={level+1}, Tries={tries[level]}, Success rate={successrate:.0f}%, Correct sequence={sequence}" )
        print( "Expression:\n-----\n\033[1m"+expression+"\033[0m\n-----" )
        correct = eval( expression )
        answ = get_input()
        if answ in ["E", "END"]:
            break
        if (( answ == "T" or answ == "TRUE" ) and correct) or \
           (( answ == "F" or answ == "FALSE" ) and not correct ):
            print("\033[92mCorrect\033[0m")
            sequence = add_one(sequence)
            success[level] += 1
        else:
            print("\033[91mIncorrect\033[0m")
            sequence = 0
        tries[level] += 1
        if sequence >= MAX_SEQUENCE:
            sequence = 0
            level = add_one(level)
            if level > MAX_COMPLEXITY:
                level = level - 1
                break
            print( "\n\x1b[6;30;42mNext level!\x1b[0m\n" )
    print( "\nFinal results:" )
    for i in range(level+1):
        if success[i]>0:
            #successrate = success[i]/tries[i]*100
            successrate = calc_success_rate( success[i], tries[i] )
        else:
            successrate = 0
        print( f"Level = {i+1}, Tries = {tries[i]}, Success rate = {successrate:.0f}%" )

def instruction():
    print(  )
    print("This is the Random Boolean Expression Challenge.")
    print(f"You will be given {MAX_COMPLEXITY} levels of complexity.")
    print(f"You must achieve a sequence of {MAX_SEQUENCE} correct answers to advance to the next level.")
    print("Reminder: Python operator precedence is (), not, and, or" )
    print("Read more at:")
    print("    https://docs.python.org/3/reference/expressions.html#boolean-operations" )
    print("    https://docs.python.org/3/reference/expressions.html#operator-precedence" )
    print("© Ojars, 2024")
    print(  )

def main():
    instruction()
    exercise()
    input("Press Enter to quit")

if __name__ == "__main__":
    main()
