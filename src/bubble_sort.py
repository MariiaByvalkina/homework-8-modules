
def bubble_sort(a):
    for p in range(len(a)+1):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a

