##Create user account
while True:
    print("Welcome to Top Take Away!")
    print("To continue please choose an option: ")
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
        break
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Create menu options and store on file with username
with open("order.txt", "a") as f:
    f.write("\n" + "\n" + username + ":" "\n")
while True:
    print("Welcome, " + username + "!")
    print("Here are the available cuisines:")
    print("1. Italian")
    print("2. Chinese")
    print("3. Mexican")
    print("4. Continue to payment")
    cuisine_choice = input("Enter the number of the cuisine you want to order from: ")

    if cuisine_choice == "1":
        # Italian cuisine
        print("Italian Menu:")
        print("1. Pizza")
        print("2. Pasta")
        dish_choice = input("Enter the number of the dish you want to order: ")
        with open("order.txt", "a") as file:
            file.write("Italian: ")
            if dish_choice == "1":
                file.write("Pizza,")
            elif dish_choice == "2":
                file.write("Pasta,")
            else:
                print("Invalid dish choice.")

    elif cuisine_choice == "2":
        # Chinese cuisine
        print("Chinese Menu:")
        print("1. Fried Rice")
        print("2. Sweet and Sour Chicken")
        dish_choice = input("Enter the number of the dish you want to order: ")
        with open("order.txt", "a") as file:
            file.write("Chinese: ")
            if dish_choice == "1":
                file.write("Fried Rice,")
            elif dish_choice == "2":
                file.write("Sweet and Sour Chicken,")
            else:
                print("Invalid dish choice.")

    elif cuisine_choice == "3":
        # Mexican cuisine
        print("Mexican Menu:")
        print("1. Tacos")
        print("2. Burritos")
        dish_choice = input("Enter the number of the dish you want to order: ")
        with open("order.txt", "a") as file:
            file.write("Mexican: ")
            if dish_choice == "1":
                file.write("Tacos,")
            elif dish_choice == "2":
                file.write("Burritos,")
            else:
                print("Invalid dish choice.")

    elif cuisine_choice == "4":
        break

    else:
        print("Invalid cuisine choice.")

# Payment & Address