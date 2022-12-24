class Solution: 
    def select(self, arr, i):
        n = 5
        arr = [4,1,3,9,7]
        # code here 
    
    def selectionSort(self, arr,n):
        for j in range(0, n-1):
            minElement =j
            for i in range(j+1,n):
                if (arr[i] < arr[minElement]):
                    minElement = i;
            if (minElement != j):
                arr[j], arr[minElement] = arr[minElement], arr[j]

        #code here
