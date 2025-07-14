

arr = [5 , 4, 3, 2, 1]

for i in range(len(arr)-1):
    print(f"\n🔁 Pass {i + 1} start:")
    for j in range(len(arr)-1):
        print(f"  Comparing: {arr[j]} & {arr[j + 1]}", end="  ")
        if arr[j] > arr[j + 1]:
            arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
            print("→ Swapped", arr)
    print(arr)