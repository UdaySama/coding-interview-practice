principal, rate, time = 1000, 5.0, 2

amt = principal * ((1 + rate / 100) ** time)

ci = round (amt - principal, 2)

print(ci)