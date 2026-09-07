# Task 1 — Basic Dictionary

student = {
    "name": "Amey",
    "age": 25,
    "city": "Latur"
}
print(student["name"])
print(student["age"])
print(student["city"])
student["language"]="Python"
student["city"]="Pune"
print(student)
print("=============Task 2 — Dictionary Methods====================")
# Use .get() to get "email".
# Use .get() to get "email" with default value "Not provided".
# Check whether "age" exists.
# Check whether "email" exists.

print(student.keys())
print(student.values())
print(student.items())
# print(student["email"])
print(student.get("email", "Not provided"))
student["email"]="ameyz@gmail.com"
if "email" in student:
    print("Email exists")
else:
    print("Email does not exist")

if "age" in student:
    print("Age exists")
else:
    print("Age does not exist")