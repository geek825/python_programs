# #Bubble sort
# list1 = [0,25,21,45,12,45,90]
 
# for j in range(len(list1)-1):
#     for i in range(len(list1)-1):
#         if list1[i]>list1[i+1]:
#             list1[i],list1[i+1] = list1[i+1],list1[i]    
# print(list1)



#selection sort
# list1 = []
# num=int(input("enter the number of elements"))
# print("The number of element are : ", num)
# for i in range(num):
#     list1.append(int(input()))
# for  i in range(len(list1)):
#     min_val = min(list1[i:])
#     min_index =list1.index(min_val,i)
#     list1[i],list1[min_index] = list1[min_index], list1[i]
    
# print(list1)

#selection sort without using min function
# list1 = []
# num = int(input("Enter the number of elements : "))

# for i in range(num):
#     list1.append(int(input()))
    
# for i in range(len(list1)):
#     min_index = i
#     for j in range(i+1,len(list1)):
#         if list1[j] < list1[min_index]:
#             min_index = j
            
#             list1[i], list1[min_index] = list1[min_index] , list1[i]
# print(list1)


#Insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key =  arr[i]
        j = i-1
    
   
        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            i -= 1
            arr[j + 1] = key
arr = [2,4,5,3,1]
insertion_sort(arr)
print("Sorted array : ",arr)