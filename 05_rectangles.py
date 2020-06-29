# **** Functions ****


# square height and base function

def rectangle_formula():
    width = float(input("Width length?: "))
    height = float(input("Height length?: "))
    var_area = width * height
    var_perimeter = (width + height) * 2

    return [var_area, var_perimeter]

# *** Main Routine starts here ***

valid_shapes = ["square", "rectangle", "triangle", "circle"]

shape = "rectangle"

print("You chose:", shape)

if shape == "rectangle":
    rectangle_ans = rectangle_formula()
    area = rectangle_ans[0]
    perimeter = rectangle_ans[1]
    print("Area: {:.2f} | Perimeter: {:.2f}".format(area, perimeter))

elif shape == "rectangle":
    print("you have selected rectangle")
