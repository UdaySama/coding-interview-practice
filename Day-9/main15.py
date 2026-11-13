arr = [5,7,1,4,0,24]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    out , i, j = [], 0, 0
    while i < len(left)  and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]);j += 1
    return out + left[i:] + right[j:]

print(merge_sort(arr))
