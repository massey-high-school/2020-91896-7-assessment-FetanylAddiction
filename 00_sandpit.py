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