# import heapq as hap

# heap = []

# hap.heappush(heap ,  10)
# hap.heappush(heap , 20)
# hap.heappush(heap  , 30)

# print(heap)

# print("after pop")

# hap.heappop(heap)
# print(heap)



# graph = {
    
#     'A' : {'B' : 1 , 'C' : 4},
#     'B' : {'A' : 1 , 'C' : 2 , 'D' : 5},
#     'C' : {'A' : 4 , 'B' : 2 , 'D' : 1},
#     'D' : {'B' : 5 , 'C' : 1}
# }

# print(graph)



# num = int(input("Enter aa number :"))

# reverse= 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
    
# print(reverse)

import calendar
year = int(input("Enter a year :"))
print(calendar.calendar(year))

