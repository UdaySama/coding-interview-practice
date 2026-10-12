password = input("Entre a new Password")


if len(password) < 6:
    print("Weak Password: Must be at least 6 characters long")
elif len(password) < 10:
    print("Moderate Password: Consider adding more characters.")
else:
    print("Strong Password")