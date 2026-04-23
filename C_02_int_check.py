
exit_code = 'xxx'

def int_check(question):
    error = "Please enter an integer between 1 and 100."
    high = 100
    low = 1

    while True:
        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        # check for inf mode / exit code
        if to_check == exit_code:
            return exit_code

        try:
            response = int(to_check)

            if response < low or response > high:
                print(error)
            # if the response is valid, return it
            else:
                return response


        except ValueError:
            print(error)
