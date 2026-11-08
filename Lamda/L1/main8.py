socres = {"Aman":5, "Sudagar":15,"Kuldeep":2}


filter_dict = dict(filter(lambda item: item[1] > 3, socres.items()))

print(filter_dict)