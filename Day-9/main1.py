arr = [5,2,9,1,5,6]

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a

print(selection_sort(arr))