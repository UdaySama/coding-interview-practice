def sort_dict_by_value(d):
    return dict(sorted(d.items(), key = lambda item: item[1]))

print(sort_dict_by_value({'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}))