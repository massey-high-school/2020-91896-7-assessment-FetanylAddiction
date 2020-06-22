# Number Checking Function


def int_check(question, low, high):
    error = "Please enter an number that is between {} and {}".format(low, high)

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def square():
    if var_num == 1:
        return "Square"


def rectangle():
    if var_num == 2:
        return "Rectangle"


def triangle():
    if var_num == 3:
        return "Triangle"


def circle():
    if var_num == 4:
        return "Circle"


# Main Routine
print("Please choose one of the numbers below to select a number")

print()
print("Square = 1")
print("Rectangle = 2")
print("Triangle = 3")
print("Circle = 4")
print()
var_num = int_check("Please Select a shape: ", 1, 4)

answer = ""

if var_num == 1:
    answer = square()

if var_num == 2:
    answer = rectangle()

if var_num == 3:
    answer = triangle()

if var_num == 4:
    answer = circle()

print("You have selected: {}".format(answer))
