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
        print("Square")


def rectangle():
    if var_num == 2:
        print("Rectangle")


def triangle():
    if var_num == 3:
        print("Triangle")


def circle():
    if var_num == 4:
        print("Circle")


# Main Routine
print("Please select one of the corresponding",
      "numbers provided to choose a shape")
print()
print("Square = 1")
print("Rectangle = 2")
print("Triangle = 3")
print("Circle = 4")
print()
var_num = int_check("Please Select a shape: ", 1, 4)

print("You have selected: {}".format(square(), rectangle(), triangle(), circle()))
