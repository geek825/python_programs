arr = []
arr2 = []
arr3 =[]
arr4 = []
num = int(input("Enter the number : "))

for i in range(1, num + 1):
  arr.append(i)

  if i% 2 == 0 and i% 3 == 0:
    arr2.append(i)

  elif i%2 == 0 :
    arr3.append(i)

  else:
    arr4.append(i)
  

print("divisible by 2 and 3" , arr2)
print("divisible by 2" , arr3)
print("not divisibe number", len(arr4))