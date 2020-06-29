# input checker function


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


# square input


def square_formula():
    side = float(input("Side length?"))
    var_area = side * side
    var_perimeter = side * 4

    return [var_area, var_perimeter]


# rectangle input


def rectangle_formula():
    width = float(input("Width length?: "))
    height = float(input("Height length?: "))
    var_area = width * height
    var_perimeter = (width + height) * 2

    return [var_area, var_perimeter]


# triangle input


def triangle_formula():
    height = float(input("Height length?: "))
    length = float(input("Base Length?"))
    var_area = length / 2 * height
    var_perimeter = height * 2 + length

    return [var_area, var_perimeter]


# circle input


pi = 3.14


def circle_formula():
    radius = float(input("What is the Radius?: "))
    var_area = pi * radius * radius
    var_perimeter = 2 * pi * radius

    return [var_area, var_perimeter]


# Main Routine

var_num = int_check("Enter a number between 1 and 4: ", 1, 4)

valid_shapes = ["square", "rectangle", "triangle", "circle"]

# shape response
print("You chose:", shape)

if shape == "square":
    square_ans = square_formula()
    area = square_ans[0]
    perimeter = square_ans[1]
    print(square_ans)

elif shape == "rectangle":
    print()