def countingSort(arr):
    # Write your code here
    result = []
    for i in range(100):
        result.append(0)
    for i in range(0, len(result)):
        count = 0
        for j in arr:
            if j == i:
                count += 1
        result[i]=count
    return (result)

