def max_value_key(d):
    return max(d, key=d.get)

print(max_value_key({'Alice': 85, 'Bob': 92, 'Charlie': 78}))