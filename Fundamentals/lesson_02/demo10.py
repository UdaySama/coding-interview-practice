class SmartBulb:

  def __init__(self, room):
    self.room = room
    self.is_on = False

  def toggle(self):
    self.is_on = not self.is_on
    state = "ON" if self.is_on else "OFF"
    return f"{self.room} bulb is now {state}."


bulb = SmartBulb(room="Living Room")
print(bulb.toggle())