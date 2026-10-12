temp = float(input("Entre temp. value:- "))
unit = input("Convert to (C)elcius or (F)ahrenheit?").split().upper()

if unit == "C":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celsius:.2f}°C")
elif unit == "F":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°F is equal to {fahrenheit:.2f}°F")
else:
    print("Invalid Choose")