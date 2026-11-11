marks = {
    "Amey":85,"sidharth":90, "sanmathi":70
}

result = dict(
    sorted(marks.items(),key=lambda x :x[1])
)
print(result)