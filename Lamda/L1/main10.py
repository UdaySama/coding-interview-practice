prices = {"Apple" : 2, "Banana": 1, "Orange": 3}
double_Prices = dict(map(lambda item:(item[0], item[1] * 2), prices.items()))
print(double_Prices)