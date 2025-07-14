def binary_search(arr , target):
    start = 0 
    end = len(arr) - 1
    
    while start <= end :
        mid = (start + end) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
target = 5

result = binary_search(arr , target)

if result != -1:
    print(result)
else:
    print("Target not found ")
w
