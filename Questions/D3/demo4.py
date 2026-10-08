"""
3. Pyramid / Equilateral Triangle Pattern

    *
   ***
  *****
 *******
*********

"""


n = 5

for i in range(n):
    print("  " * (n - i - 1), end="")

    print("* " * (2 * i + 1))