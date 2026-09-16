def validate_amount(text):
    while True:
        user_input = input(text)
        try:
            user_input = float(user_input)
            return user_input

        except ValueError:
            print("write a valid number\n")


def validate_user_input(text, validation_option=None):

    if validation_option:
        
        while True:
            user_input = input(text)
            if user_input in validation_option:
                return user_input
            
            else:
                print("selection out of valid range\nChoose Again\n")
                continue
    else:
        user_input = input(text)
        return user_input
