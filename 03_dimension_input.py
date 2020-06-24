# **** Functions ****

# shape ask function:


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


# square height and base function

def square_formula():
    side = float(input("Side length? "))
    var_area = side * side
    var_perimeter = side * 4

    return [var_area, var_perimeter]


# *** Main Routine starts here ***

valid_shapes = ["square", "rectangle", "triangle", "circle"]

shape = string_checker("Choose a shape ", valid_shapes)

print("You chose:", shape)

if shape == "square":
    square_ans = square_formula()
    area = square_ans[0]
    perimeter = square_ans[1]
    print(square_ans)

elif shape == "rectangle":
    print("I'm a rectangle")
