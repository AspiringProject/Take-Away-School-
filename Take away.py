##Create user account
while True:
    print("Welcome! Please choose an option:")
    print("1. Sign up")
    print("2. Log in")
    print("3. Exit")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        # Sign up
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        with open("users.txt", "a") as file:
            file.write(username + "," + password + "\n")
        print("Sign-up successful!")
    
    elif choice == "2":
        # Log in
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        found = False
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(',')
                    if username == stored_username and password == stored_password:
                        print("Log-in successful!")
                        found = True
                        break
            if not found:
                print("Incorrect username or password.")
        except FileNotFoundError:
            print("No users found. Please sign up first.")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

##Create menu options
print("These are our menu options:")

menu = input("What menu would you like to view?")
