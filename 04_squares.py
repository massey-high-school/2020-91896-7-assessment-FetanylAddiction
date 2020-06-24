# **** Functions ****


# square height and base function

def square_formula():
    side = float(input("Side length?"))
    var_area = side * side
    var_perimeter = side * 4

    return [var_area, var_perimeter]


# *** Main Routine starts here ***

valid_shapes = ["square", "rectangle", "triangle", "circle"]

shape = "square"

print("You chose:", shape)

if shape == "square":
    square_ans = square_formula()
    area = square_ans[0]
    perimeter = square_ans[1]

elif shape == "rectangle":
    print("I'm a rectangle")
