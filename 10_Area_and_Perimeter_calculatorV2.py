# put functions here


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

# Ask user for the squares side length and calculates it
def square_formula():
    side = num_check("Side length?")
    var_area = side * side
    var_perimeter = side * 4

    return [var_area, var_perimeter]


# rectangle input function

# Ask user for the rectangle's length and height and calculates it
def rectangle_formula():
    width = num_check("Width length?: ")
    height = num_check("Height length?: ")
    var_area = width * height
    var_perimeter = (width + height) * 2

    return [var_area, var_perimeter]


# triangle input function

# Ask user for the base and height and calculates it
def triangle_formula():
    height = num_check("Height length?: ")
    base = num_check("Base Length?: ")
    var_area = base / 2 * height
    var_perimeter = height * 2 + base

    return [var_area, var_perimeter]


# circle input function

pi = 3.14


# Ask user for the radius of the circle and calculates it
def circle_formula():
    radius = num_check("What is the Radius?: ")
    var_area = pi * radius ** 2
    var_perimeter = 2 * pi * radius

    return [var_area, var_perimeter]


# ******* Main routine starts here ******
yes_no = ["square", "rectangle", "triangle", "circle", "xxx"]
shape_list = ["Square", "Rectangle", "Triangle", "Circle"]

# Make large empty list here
big_list = []

shape = ""
while shape.lower() != "xxx":
    # make / empty small list
    small_list = []
    # get user input and work out area / perimeter
    shape = string_checker("Choose a shape: ", yes_no)

    if shape == "square":
        square_ans = square_formula()
        area = square_ans[0]
        perimeter = square_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    # rectangle response

    # Prints rectangle calculator results into a list with a max of two decimal points
    elif shape == "rectangle":
        rectangle_ans = rectangle_formula()
        area = rectangle_ans[0]
        perimeter = rectangle_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    # triangle response

    # Prints triangle calculator results into a list with a max of two decimal points
    elif shape == "triangle":
        triangle_ans = triangle_formula()
        area = triangle_ans[0]
        perimeter = triangle_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    # circle response

    # Prints circle calculator results into a list with a max of two decimal points
    elif shape == "circle":
        circle_ans = circle_formula()
        area = circle_ans[0]
        perimeter = circle_ans[1]
        print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

    # add stuff to small list
    small_list.append(shape)
    small_list.append(area)
    small_list.append(perimeter)
    # add small list to large list

    big_list.append(small_list)

print(big_list)
