def insertionSort1(n, arr):
    # Write your code here
    memory=arr[-1]
    i=n-1
    while i>0 and arr[i-1]>memory:
        arr[i]=arr[i-1]
        print(*arr)
        i-=1
    arr [i]=memory
    print(*arr)