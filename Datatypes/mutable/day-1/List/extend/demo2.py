def interleave_batches(l1,l2):
    res = []
    for a,b in zip(l1,l2):
        res.extend([a,b])
    return res


print(interleave_batches([1, 3], [2, 4]))