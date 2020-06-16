# Number Checking Function
def int_check(question, low, high):
    error = "Please enter an number that is between {} and {}".format(low, high)

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:

                print(error)

        except ValueError:
            print(error)

# Main Routine

var_num = int_check("Enter a number between 1 and 4: ", 1, 4)
