def collect_keys(lst,d):
    lst.extend(d.keys())
    return lst


print(collect_keys(["id"], {"name": "Alice", "age": 25}))