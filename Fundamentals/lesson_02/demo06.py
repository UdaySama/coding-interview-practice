class Smartphone:

  def __init__(self, brand, battery=100):
    self.brand = brand
    self.battery = battery

  def use_phone(self, hours):
    self.battery = max(0, self.battery - (hours * 10))
    return f"Battery left: {self.battery}%"


phone = Smartphone(brand="Samsung")
print(phone.use_phone(3))