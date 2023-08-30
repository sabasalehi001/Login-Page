def login():
    saved_username = "john"  # Predefined username
    saved_password = "password123"  # Predefined password

    # Input username from the user
    username = input("Enter your username: ")
    # Input password from the user without displaying it on the screen
    password = input("Enter your password: ")

    # Check if the entered username and password match the saved username and password
    if username == saved_username and password == saved_password:
        print("Login Successful!")
    else:
        print("Invalid username or password. Please try again.")

login()
