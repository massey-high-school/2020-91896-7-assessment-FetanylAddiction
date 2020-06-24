# **** Functions ****

# shape ask function:


# square height and base function

pi = 3.14


def circle_formula():
    radius = float(input("What is the Radius?: "))
    var_area = pi * radius * radius
    var_perimeter = 2 * pi * radius

    return [var_area, var_perimeter]


# *** Main Routine starts here ***

valid_shapes = ["square", "rectangle", "triangle", "circle"]

shape = "circle"

print("You chose:", shape)

if shape == "circle":
    circle_ans = circle_formula()
    area = circle_ans[0]
    perimeter = circle_ans[1]
    print(circle_ans)

elif shape == "circle":
    print("you have selected circle")
