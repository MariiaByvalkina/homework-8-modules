def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        current = arr[0]
        less = [x for x in arr if x < current]
        equal = [x for x in arr if x == current]
        greater = [x for x in arr if x > current]
        return quick_sort(less) + equal + quick_sort(greater)


