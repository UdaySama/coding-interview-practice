a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

choice = int(input("Enter chosen number: "))

if choice == 1:
    print("Sum =", a + b)
elif choice == 2:
    print("Sub =", a - b)
elif choice == 3:
    print("Multi =", a * b)
elif choice == 4:
    if b != 0:
        print("Divi =", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Choice")