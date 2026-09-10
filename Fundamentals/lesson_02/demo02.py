class Cat:

  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.is_sleeping = False

  def nap(self):
    self.is_sleeping = True
    return f"{self.name} is now taking a nap."


my_cat = Cat(name="Whiskers", color="Gray")
print(my_cat.nap())