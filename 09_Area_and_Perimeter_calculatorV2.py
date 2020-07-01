
# print statements and shape identifiers


# put functions here


# Num_check function
def num_check(question):
    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:

        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)


# shape input & string checker function
def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response")


# square input function

def shape_formula(shape):
    if shape == "square":
        side = num_check("Side length?")
        var_area = side * side
        var_perimeter = side * 4

        return [var_area, var_perimeter]

    if shape == "rectangle":
        width = num_check("Width length?: ")
        height = num_check("Height length?: ")
        var_area = width * height
        var_perimeter = (width + height) * 2

        return [var_area, var_perimeter]

    if shape == "triangle":
        height = num_check("Height length?: ")
        base = num_check("Base Length?: ")
        var_area = base / 2 * height
        var_perimeter = height * 2 + base

        return [var_area, var_perimeter]

    elif shape == "circle":
        pi = 3.14
        radius = num_check("What is the Radius?: ")
        var_area = pi * radius ** 2
        var_perimeter = 2 * pi * radius

        return [var_area, var_perimeter]


def shape_response(shape):
    if shape == "square":
        square_ans = shape_formula(shape)
        area = square_ans[0]
        perimeter = square_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    if shape == "rectangle":
        rectangle_ans = shape_formula()
        area = rectangle_ans[0]
        perimeter = rectangle_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    if shape == "triangle":
        triangle_ans = shape_formula()
        area = triangle_ans[0]
        perimeter = triangle_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    elif shape == "circle":
        circle_ans = shape_formula()
        area = circle_ans[0]
        perimeter = circle_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))


# ******* Main routine starts here ******
yes_no = ["square", "rectangle", "triangle", "circle", "xxx"]
shape_list = ["Square", "Rectangle", "Triangle", "Circle", "xxx"]

print(shape_list)
print()

# List printer
big_list = []

var_shape = ""
while var_shape.lower() != "xxx":
    var_shape = string_checker("Choose a shape: ", yes_no)

    print("You chose:", var_shape)

    small_list = []
    # ask_user = shape_formula(var_shape)
    shape_calculation = shape_response(var_shape)

    small_list.append(ask_user)
    small_list.append(shape_calculation)

    big_list.append(small_list)
  # add small list to large list


print(big_list)
# Output large list here so that it looks nice