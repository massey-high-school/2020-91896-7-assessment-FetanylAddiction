def input_check(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # Looks for Letters and blanks in response and complains if necessary
            for letter in response:
                if letter.isalpha():
                    has_errors = "yes"
                    break
        if int(response) > 5:
            print(error)
            continue
        elif int(response) < 0:
            print(error)
        elif response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


dimension = input_check("Please enter in a  number that corresponds with a shape",
                        "Please enter in a valid number",
                        "yes")