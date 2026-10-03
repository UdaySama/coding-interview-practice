def get_Initials(names):
    ini = []
    for name in names:
        if name:
            ini.append(name[0])
    return ini


print(get_Initials(['Amey, Siddharth, Parvej']))