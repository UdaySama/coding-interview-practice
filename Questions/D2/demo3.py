raw_data= ["10", 20.5, "30", 40, "abc"]

parsed = []

for item in raw_data:
    try:
        parsed.append(int(item))
    except ValueError:
        pass


print(parsed)