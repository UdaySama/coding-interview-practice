arr = [7,3,9,0,1]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot, rest = arr[0],arr[1:]
    left = [x for x in rest if x < pivot]
    right = [x for x in rest if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))



