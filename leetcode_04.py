# Three Consecutive Odds



num = int(input("Enter the number"))

if num %2 != 0:
    for i in range(3):
        print(num + i * 2 , end=" ")
else:
    print("Enter the Valid no")