def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result



print(remove_duplicates([1,4,7,0,5,1,7,4,0]))