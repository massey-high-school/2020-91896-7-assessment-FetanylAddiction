# ***** Functions *****

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

def shape_formula():
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


def shape_response():
    if shape == "square":
        square_ans = shape_formula()
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


# ***** Main Routine *****

# list printing system

# print statements and shape identifiers

yes_no = ["square", "rectangle", "triangle", "circle"]
shape_list = ["Square", "Rectangle", "Triangle", "Circle"]

print(shape_list)
print()

shape = string_checker("Choose a shape: ", yes_no)
print("You chose:", shape)

if shape == 'square':
    print(shape_response())

if shape == 'rectangle':
    print(shape_response())

if shape == 'triangle':
    print(shape_response())

if shape == 'circle':
    print(shape_response())
