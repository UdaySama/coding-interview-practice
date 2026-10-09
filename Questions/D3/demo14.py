def removeDuplicatesPreserveOrder(lst):
    seen = set()
    res = []
    for itM in lst:
        if itM not in seen:
            seen.add(itM)
            res.append(itM)
    return res

print(removeDuplicatesPreserveOrder([3, 1, 2, 3, 4, 1, 5]))