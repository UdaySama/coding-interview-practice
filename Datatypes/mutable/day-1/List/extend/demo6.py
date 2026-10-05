def compare_append_extend(ba1,ba2,itM):
    ba1.append(itM)
    ba2.extend(itM)
    return ba1,ba2


print(compare_append_extend([1, 2], [1, 2], [3, 4]))