import random
"""
This app allows a user to log in to password manager and access the following;
- A password generator that will create a unique password, with character length specified by user, consisting of 
randomly generated uppercase letters, lowercase letters, symbols and numbers.
- A PIN generator, should the user wish to access a randomly generated numerical sequence, of a specific length
- The option to save any generated passwords, and assign them to a keyword
- A password library where the user can obtain previously saved passwords by searching for the keyword they linked
that password to.
"""
USER_NAME = "Code In Place"
PASSWORD = "Stanford"


def main():
    password_library = {}  # create empty dictionary for generated passwords
    login_to_password_manager()  # Grants access to app if details are correct
    # Providing the user enters correct login details, they will then be granted access to the startup menu
    password_manager_startup(password_library)


def login_to_password_manager():
    enter_username = input("Please enter your username: ")
    enter_password = input("Please enter your password: ")
    print("")
    #  Pass username, enter_username, password, enter_password into 'check details' to perform security check
    check_details(enter_username, enter_password)


def check_details(enter_username, enter_password):
    if USER_NAME == enter_username:
        if PASSWORD == enter_password:
            print("Welcome to password manager!")  # User accesses password_manager_startup
        else:
            print("Your details are incorrect, please enter them again.")  # Password incorrect
            #  User taken back to login stage
            login_to_password_manager()
    else:
        print("Your details are incorrect, please enter them again.")  # Username incorrect
        #  User taken back to login stage
        login_to_password_manager()


def password_manager_startup(password_library):
    #  User now has the option to choose whether they want to create a password, or access previously saved passwords
    print("Would you like to create a new password, or access your existing passwords?")
    print("")
    #  While loop used to repeat options to user should they enter an invalid choice
    user_input = None
    while not user_input:
        user_input = int(input("Enter 1 to create a password, or 2 to access your password library: "))
        print("")
        if user_input == 1:
            password_generator_startup(password_library)
        elif user_input == 2:
            access_password_library(password_library)
        else:
            print("Please enter a valid choice")
            print("")
            user_input = None


#  Password library passed into function, to enable user to save the generated password should they wish
def password_generator_startup(password_library):
    print("Let's get started! Do you need to create a password or a pin?")
    print("* * * A password will contain a combination of letters, numbers and symbols."
          " A pin will contain only numbers * * *")
    print("")
    user_selection = None
    while not user_selection:
        #  When user enters a valid choice, while loop breaks as user_selection = True
        user_selection = int(input("Enter 1 to create a password, or 2 to create a pin: "))
        print("")
        if user_selection == 1:
            password_generator(password_library)
        elif user_selection == 2:
            pin_generator(password_library)
        else:  # If user enters anything other than 1 or 2, while loop continues to run
            print("Please make a valid choice")
            user_selection = None
    print("")


def access_password_library(password_library):
    user_input = None
    while not user_input:
        password_search = input("Which password would you like to retrieve?: ")
        print("Your password for " + str(password_search) + " is: " + str(password_library.get(password_search)))
        print("")
        user_input = input("Press return to access another password, or any other key to return to password"
                           " generator: ")
        print("")
    password_generator_startup(password_library)


def password_generator(password_library):
    print("How many characters should I put into your password?")
    #  User to choose password length. Convert to integer value.
    password_length = int(input("Enter the number of characters required: "))
    print("")
    create_password(password_length, password_library)  # Pass chosen password length into create password function


def create_password(password_length, password_library):
    random_password = []  # Create empty list for password
    for i in range(password_length):
        elem = random.randint(33, 122)  # 33-122 is relative to Ascii values for symbols, letters & numbers
        random_password.append(elem)  # Append random number to list
    new_password = ""  # Create empty string to append characters in password to once generated
    for values in random_password:
        new_password += chr(values)  # Convert numbers in list to relevant Ascii characters
    print("New password: " + str(new_password))  # Password printed as Ascii characters
    print("")
    print("Where will you be using this password?")
    site = input("Please type the application you will be using this password for: ")
    password_library[site] = new_password
    print("Your new password has been saved!")
    print("")
    password_manager_startup(password_library)


def pin_generator(password_library):
    print("How many numbers should I put into your pin?")
    pin_length = int(input("Enter the length of pin required: "))  # User to select how many numbers their pin requires
    print("")
    create_pin(pin_length, password_library)  # Pin length passed into create_pin function


def create_pin(pin_length, password_library):
    pin = []  # Blank list created for pin
    for i in range(pin_length):
        num = random.randint(1, 9)
        pin.append(num)  # Append random number to list
    new_pin = ""
    for values in pin:
        new_pin += str(values)  # Append randomly generated integers to empty string
    print("New pin: " + str(new_pin))  # Print integers as string
    print("")
    print("Where will you be using this PIN?")
    site = input("Please type the application you will be using this PIN for: ")
    password_library[site] = new_pin
    print("Your new PIN has been saved!")
    print("")
    password_manager_startup(password_library)


if __name__ == '__main__':
    main()