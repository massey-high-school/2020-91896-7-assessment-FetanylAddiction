# **** Functions ****

# shape ask function:


# square height and base function

def triangle_formula():
    height = float(input("Height length?: "))
    length = float(input("Base Length?"))
    var_area = length / 2 * height
    var_perimeter = length + height * 2

    return [var_area, var_perimeter]

# *** Main Routine starts here ***

valid_shapes = ["square", "rectangle", "triangle", "circle"]

shape = "triangle"

print("You chose:", shape)

if shape == "triangle":
    triangle_ans = triangle_formula()
    area = triangle_ans[0]
    perimeter = triangle_ans[1]
    print(triangle_ans)

elif shape == "triangle":
    print("you have selected triangle")
