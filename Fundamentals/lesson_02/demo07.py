class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width


rect = Rectangle(length=10, width=5)
print(f"Area: {rect.area()}")