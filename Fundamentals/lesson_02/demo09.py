class Coffee:

  def __init__(self, flavor, size):
    self.flavor = flavor
    self.size = size

  def get_receipt(self):
    price = 4.00 if self.size == "Large" else 3.00
    return f"{self.size} {self.flavor} Coffee: ${price}"


order = Coffee(flavor="Latte", size="Large")
print(order.get_receipt())