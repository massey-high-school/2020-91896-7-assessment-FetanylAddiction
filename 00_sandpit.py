big_list = []

name = ""
if name == 'main':
    while name != "xxx":

        row_list = []

        name = input("who are you: ")
        if name.lower() == "xxx":
            break

        age = int(input("Age: "))
        colour = input("Favourite colour")

        row_list.append(name)
        row_list.append(age)
        row_list.append(colour)

        big_list.append(row_list)

# output data..
# see last video of epub for sorting

for item in big_list:
    print(item)

# random list thingy
big_list = []

shape = ""
if shape == 'main':
    while shape != "xxx":

        row_list = []

        shape = input("what is your shape?: ")
        if name.lower() == "xxx":
            break

        base = int(input("what is your base?: "))
        width = input("what is your width?:")

        row_list.append(name)
        row_list.append(base)
        row_list.append(width)

        big_list.append(row_list)

# output data..
# see last video of epub for sorting

for item in big_list:
    print(item)


if shape == 'square':
    print(shape_response())

if shape == 'rectangle':
    print(shape_response())

if shape == 'triangle':
    print(shape_response())

if shape == 'circle':
    print(shape_response())
