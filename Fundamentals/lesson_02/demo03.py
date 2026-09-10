class Car:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.speed = 0

  accelerate = lambda self, increment: setattr(
      self, "speed", self.speed + increment
  )


my_car = Car(brand="Toyota", model="Corolla")
my_car.accelerate(30)
print(f"{my_car.brand} speed: {my_car.speed} km/h")