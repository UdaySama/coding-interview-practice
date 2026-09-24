yr = 2024

if(yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    result = "Leap year"
else:
    result = "Not a Leap year"

print(result)

