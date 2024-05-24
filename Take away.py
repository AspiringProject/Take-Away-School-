##Create user account
sign = "qwerty"

print("Welcome to Top Take-Away")
existing = input("Have you signed in before?:")

if existing.lower() == "no":
    print("You must register for an account before you can continue")

    namef = input("What is your first name?: ")
    namel = input("What is your last name?: ")
    dob = input("What is your year of birth?: ")

    userpass = namef[0]+namel+dob[2]+dob[3]
    print("Your password is:",userpass)

    open("userpass.txt", "w")
    file.write(userpass)

elif existing.lower() == "yes":
    open("userpass.txt", "a")

##Create menu options
print("These are our menu options:")

menu = input("What menu would you like to view?")
