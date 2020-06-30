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

# ***** Main routine *******
base = num_check("What is the base? ")
print(base)