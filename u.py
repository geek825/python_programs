list1 = [1 , 2, 3, 4, 5]
list2 =[]
idex = int(input("Enter the number you want to delete"))
for i in list1:
    list1.pop(idex)
list2.append(list1)

print(list2)

