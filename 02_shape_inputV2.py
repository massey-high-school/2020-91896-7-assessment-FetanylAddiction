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


# *** Main Routine starts here ***

yes_no = ["square", "rectangle", "triangle", "circle"]


shape = string_checker("Choose a shape ", yes_no)


print("You chose:", shape)

