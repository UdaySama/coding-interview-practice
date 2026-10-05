def flatten(mat):
    flat = []
    for row in mat:
        flat.extend(row)
    return flat


print(flatten([[1, 2], [3, 4], [5]]))