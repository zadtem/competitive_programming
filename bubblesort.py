def countSwaps(a):
    count = 0
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    
    print("Array is sorted in", count, "swaps." )
    print("First Element:", a[0])
    print("Last Element:", a[-1])
