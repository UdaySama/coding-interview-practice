def create_matrix(r,c):
    m = []
    for i in range(r):
        r = []
        for j in range(c):
            r.append(i * c + j)
            m.append(r)
    return m


print(create_matrix(2,3))