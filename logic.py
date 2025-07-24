

# # 1 Find the digital root of a number

# # def digital_root(n):
# #     while n >= 10:
# #         sum_digits = 0 
# #         while n > 0:
# #             sum_digits += n %10
# #             n = n // 10
# #         n = sum_digits 
# #     return n
# # n = int(input("Enter a number : "))
# # result = digital_root(n)
# # print("Digital root is : ", result)

# # 2 count trailing 
# # def count_trilling(n):
# #     i = 5
# #     count = 0
    
# #     while n //  i > 0:
# #         count += n // i
# #         i *= 5
# #     return count 
# # n  = int(input("Enter the number : "))
# # result = count_trilling(n)
# # print(result)

# # 3 Rotate an array by k elements

# # def rotate_array(arr  , k):
# #     n = len(arr)
# #     l = k % n
# #     rotate = arr[-l:] + arr[:-l]
# #     return rotate

# # arr = [1 ,2 ,3,4,5,6]
# # k = 3
# # result = rotate_array(arr , k)
# # print(result)

# # 4 valid paranthesis

# # def valid_pranthisis(s):
# #     stack = []
# #     pairs = {')':'(' , '}' : '{ ' , ']' : '[' }  
    
# #     for char in s:
# #         if char in pairs.values():
# #             stack.append(char)
# #         elif char in pairs.keys():
# #             if not stack or stack[-1] != pairs[char]:
# #                 return False
# #             stack.pop()
# #     return not stack
            
# # s = input("Enter : ")
# # result = valid_pranthisis(s)

# # if result:
# #     print("Valid Pranthisis")
# # else:
# #     print("Invalid pranthisis")


# # 5 second largest number in array

# # num = [22 , 34 ,23 ,44]
# # set_num = sorted((set(num))[-2])
# # print("Second Largest Number is : " , set_num)

# # sentance = "Hello world"
# # words = sentance.split()

# # print("number of the words : ", len(words))

# # 6 GCD of two numbers 

# # a ,b = 5 , 10
# # while b :
# #     a , b = b , a % b
# # print("GCD is :" , a)

# # 7 Reverse a number and string
# # num = 123
# # reverse = 0 

# # while num > 0:
# #     digit = num % 10
# #     reverse = reverse * 10 + digit 
# #     num = num // 10
    
# # print("Reversed Number is :" , reverse)


# # s = "Hello"
# # rev = "" 
# # for char in s:
# #     rev = char + rev

# # print("Reversed String is :" , rev)

# # 8 Count of vowels and consonants

# # word = input("Enter the sentance : ")
# # vowels = "aeiouAEIOU"
# # count = 0
# # consatant = 0
# # for ch in word :
# #     if ch in vowels:
        
# #         count += 1
        
# #     else:
# #         consatant += 1
        
# # print("Vowels count" , count)
# # print("Consatant count" , consatant)

# # 9 Remove dublicates form string

# # string = input("Enter string : ")
# # list2 = []

# # for ch in string:
# #     if ch not in list2:
# #         list2.append(ch)
# # print(list2)


# # 10 binary search
# # def binary_search(arr , target):
# #     arr.sort()
# #     start = 0 
# #     end = len(arr) - 1
    
# #     while start <= end :
# #         mid = (start + end ) // 2
        
# #         if arr[mid] == target :
# #             return mid
            
# #         elif arr[mid] < target :
# #             start = mid + 1
            
# #         else:
# #             end = mid - 1
            
# #     return - 1

# # arr = [22 , 43 , 12 , 54 ,13]
# # target = 43

# # index = binary_search(arr , target)

# # if index != -1:
# #     print(index)
# # else:
# #     print("Index no found")


# # 11 number to binery

# # def number_to_binery(num) :
# #     binery = ""
    
# #     while num > 0:
# #         remainder = num % 2
# #         binery = str(remainder) + binery 
# #         num = num //2
        
# #     return binery
# # num = int(input("Enter the number :"))
# # result = number_to_binery(num)

# # print(result)
    
# # 12 binery to number
   
# # def binery_to_number(num):
# #     decimal = 0
# #     power = 0
    
# #     for digit in reversed(num):
# #         if digit == '1':
# #             decimal += 2 ** power
# #         power += 1
        
# #     return decimal
    
# # num = "11010"

# # result = binery_to_number(num)

# # print(result)

# # 13 selction sort

# # def selection_sort(arr):
    
# #     n  = len(arr)
    
# #     for i in range(n):
# #         min_index = i 
        
# #         for j in range(i + 1 , n):
# #             if arr[j] < arr[min_index]:
# #                 arr[j] , arr[min_index] = arr[min_index] , arr[j]
                
# # arr = [12 , 2  , 45 , 23 , 32 ]
# # selection_sort(arr)
# # print(arr)

# # 14 sum of digits

# # num = 111
# # sum1 =0

# # while num > 0 :
# #     digit = num % 2
# #     sum1 += digit

# # print(sum1)

# # 15 digit root

# # def Digital_root(n):
# #     while n >=10:
# #         sum1 = 0
# #         while n > 0:
# #             sum1 += n % 10
# #             n = n // 10
            
# #         n = sum1
# #     return n 
    
    
# # num = int(input("Enter the number : "))
# # result = Digital_root(num)
# # print("Digital root of the number is :" , result)

# # 16 matrix

# # rows = int(input("Enter the row number :"))
# # cols = int(input("Ener the colum number :"))

# # matrix = []
# # total = 0
# # print("Enter the number row wise :")
# # for i in range(rows):
# #     row = list(map(int , input("Enter").split()))
# #     if len(row) != cols:
# #         print("Error")
# #         exit()
# #     matrix.append(row)

# # print("\nmatrix is :")
# # total = 0
# # for rows in matrix:
# #     for element in rows:
# #       total += element 
       
       
# # for row in matrix : 
# #     print(*row)
    
# # 17 longesht word

# # sentence = "yash shelar programming"
# # word = ""
# # longest = ""

# # for char in sentence :
# #     if char != " ":
# #         word += char
        
# #     else:
# #         if len(word) > len(longest):
# #             longest = word
        
# #         word = ""
    
# # if len(word) > len(longest):
# #     longest = word
    
# # print("The longest word is " , longest)

# # 18 toggle

# # sentance = "YAsh ShElAr"
# # toggle = "" 

# # for char in sentance :
# #     if char.isupper() :
# #         toggle += char.lower()
        
# #     elif char.lower():
# #         toggle += char.upper()
        
# #     else:
# #         toggle += char
        
# # print(toggle)

# # 19 pangram

# # string = input("Enter string : ")
# # string_set = set(string)

# # for char in string.lower():
# #     if char.isalpha():
# #         string_set.add(char)
        
# # if len(string_set) == 26:
# #     print("string is pangram")
    
# # else:
# #     print("string is not a pangram")
    
# # 20 second largest 
    
# # arr = [22 , 34 , 21 , 4 ,12]

# # for i in range(len(arr)) :
# #     for j in range(i + 1 , len(arr)):
# #         if arr[i] > arr[j] :
# #             arr[i] , arr[j] = arr[j] , arr[i]
# # print(arr)           
# # print( "The second largest number is " , arr[-2])

# # 21 second smallest

# # arr = [22 , 34 , 21 , 4 ,12]

# # for i in range(len(arr)) :
# #     for j in range(i + 1 , len(arr)):
# #         if arr[i] > arr[j] :
# #             arr[i] , arr[j] = arr[j] , arr[i]
# # print(arr)           
# # print( "The second smallest number is " , arr[1])

# # 22 merge sorted arr
# # arr = [22 , 34 , 21 , 4 ,12]

# # for i in range(len(arr)) :
# #     for j in range(i + 1 , len(arr)):
# #         if arr[i] > arr[j] :
# #             arr[i] , arr[j] = arr[j] , arr[i]
         
# # print( "The sorted array is : " , arr)



# # arr = [22 , 34 , 21 , 4 ,12]
# # arr3 = []
# # for i in range(len(arr)) :
# #     for j in range(i + 1 , len(arr)):
# #         if arr[i] > arr[j] :
# #             arr[i] , arr[j] = arr[j] , arr[i]
         

# # arr2 = [50 , 35 , 22 , 5 ,13]

# # for i in range(len(arr2)) :
# #     for j in range(i + 1 , len(arr2)):
# #         if arr2[i] > arr2[j] :
# #             arr2[i] , arr2[j] = arr2[j] , arr2[i]
         

# # merge = arr + arr2 

# # for i in range(len(merge)):
# #     for j in range(i + 1 , len(merge)):
# #         if merge[i] > merge[j]:
# #             merge[i] , merge[j] = merge[j] , merge[i]
            
            
# # for i in merge : 
# #     if i not in arr3:
# #         arr3.append(i)
        
# # print("After remove dublicates array is :" , arr3)


# # 22 rotate array k times

# # def rotate_array(arr , k) :
# #     n = len(arr)
# #     l = k % n 
    
# #     rotate = arr[-l:] + arr[:-l]
# #     return rotate
    
# # arr = [22 , 34 , 12 , 4 , 7]
# # k = 3
# # result = rotate_array(arr , k)

# # print(result)

# # 23 armstrong number

# # num = int(input("Enter a number :"))

# # def is_armstrong(num):
# #     sum1 = 0
# #     temp = num
# #     while temp > 0:
# #         digit = temp % 10
# #         sum1 += digit ** 3
# #         temp = temp //  10

# #     return sum1 == num
# # result = is_armstrong(num)    

# # if  result:
# #     print("The number is armstrong")
    
# # else:
# #     print("The number is not armstrong")

# # 24 perfect number

# # def prefect_number(num):
# #     sum1 = 0 
    
# #     for i in range( 1 , num):
# #         if num % i == 0 :
# #             sum1 += i

# #     return sum1 == num 

# # num = 6

# # result = prefect_number(num)

# # if result :
# #     print("The number is perfect number " )

# # else:
# #     print("The number is not a prefect number")    

# # 25 generte prime

# # def generate_prime(num) :
# #     prime = []
    
# #     for i in range(2 , num):
# #         for j in range(2 , int(i ** 0.5) + 1):
# #             if i % j == 0:
# #                 break
# #             else:
# #                 prime.append(i)      
# #     return prime
# # num = 10

# # result = generate_prime(num)

# # print(result)


# # num = int(input("Enter the number :"))
# # fact = 1

# # for i in range(1 , num + 1):
# #     fact *= i

# # print(fact)

# # palindrome number

# # num  = int(input("Enter the number :"))
# # original = num 

# # reverse = 0

# # while num > 0:
# #     digit = num %  10
# #     reverse = reverse * 10 + digit
# #     num = num // 10
    
# # if original == reverse:
# #     print("the number is palindrome")
    
# # else:
# #     print("The number is not palindrome")

# # def armstrong_no(num):
# #     sum1= 0
# #     temp =num

# #     while temp > 0:
# #         digit = temp % 10
# #         sum1 += digit ** 3
# #         temp = temp // 10
        
# #     return sum1 == sum 

# # num  = int(input("Enter the number :"))
# # result = armstrong_no(num)

# # if result :
# #     print("The number is armstrong number")
# # else:
# #     print("the number is not armstrong number")



# # num =  int(input("Enter the number :"))

# # reverse = 0 

# # while num > 0 :
# #     digit = num % 10
# #     reverse = reverse * 10 + digit
# #     num = num // 10
    
# # print(reverse)


# # num  = int(input("Enter the number :"))
# # count = 0

# # while num > 0:
# #     digit = num % 10
# #     count += 1
# #     num = num // 10
    
# # print(count)

# # count words

# # def count_words(string):
# #     words = string.split()
    
# #     word_count = {}

# #     for word in words:
# #         if word in word_count:
# #             word_count[word] += 1
# #         else:
# #             word_count[word] = 1
            
# #     return word_count

# # string  = input("Enter the string :")
# # result = count_words(string)

# # print(result)   

# # Missing number

# # def missing_number(num ):
# #     n = len(num)
# #     total = (n + 1) * (n + 2) // 2
    
# #     sum1 = 0
# #     for i in num:
# #         sum1 += i 
        
# #     return total -sum1 

# # num  = [1 , 2 ,3 ,5]

# # result = missing_number(num)
# # print(result)

# # Remove zeroes

# # def remove_zeros(num):
# #     num = str(num)
    
# #     while "0" in num :
# #         num = num.replace("0" , "")
# #     return int(num)

# # num = 12002101230
# # result = remove_zeros(num)

# # print(result)        

# # similar number

# # def similar_number(list1 , list2 ):
# #     list3 =[]
# #     for i in list1:
# #         if i in list2:
# #             list3.append(i)
            
# #     return list3

# # list1 = [1 , 2 , 3 , 4]
# # list2 = [3 , 4 , 8]

# # result = similar_number(list1 , list2)
# # print(result)

# # factor of number

# # def factor_number(num):
# #     for i in range( 1 , num + 2):
# #         if num % i == 0:
# #             print(i)
            
# # num = int(input("Enter the number :"))

# # factor_number(num)


# # def pangram(s):
# #     alpha = "abcdefghijklmnopqrstuvwxyz"
    
# #     for i in alpha :
# #         if i not in s.lower():
# #             return False
# #         return True
    
# # s = "The quick brown fox jumps over the lazy dog"
# # result = pangram(s)

# # print(result)



# # def lcm(x , y):
# #     if x > y:
# #         gretar = x

# #     else:
# #         gretar = y

# #     while True :
# #         if (gretar % x == 0) and (gretar % y == 0) :
# #             lcm =gretar
# #             break

# #         gretar += 1
        
# #     return lcm

# # x = int(input("Enter the number :"))
# # y = int(input("Enter the 2nd number :"))

# # result = lcm(x , y)
# # print(result)       

# # def prime_in_range(num):
# #     for i in range(2 , num + 1):
# #         is_prime = True
# #         for j in range(2 , int(i ** 0.5) + 1):
# #             if i % j == 0 :
# #                 is_prime = False
# #                 break

# #         if is_prime:
# #             print(i)
# # num = int(input("Enter the number :"))

# # result = prime_in_range(num)

# # print(result)
                
                
# # num = int(input("Enter the number :"))

# # sum1 = 0

# # for i in range(1 , num + 1):
# #     sum1 += i   
    
# # print("The sum of natural numbers", sum1)              


# # def first_repating_char(s):
# #     char_count = {}
# #     count = 0
    
    
# #     for char in s :
# #         if char in char_count:
# #             char_count[char] += 1
# #         else:
# #             char_count [char] = 1
            
# #     for char , count in char_count.items():
# #         if count > 1:
# #             return char
  

# # def longest(s):
# #     word = s.split()
# #     longest_word = ""
    
# #     for i in word:
# #            if len(i)  > len(longest_word):
# #             longest_word = i

# #     return longest_word

# # s = "yash shelar"

# # result = longest(s)

# # print(result)

# # def find_dublicates(arr):
# #     seen = len(arr)
    
# #     for i in range(len(arr)):
# #         for j in range(i + 1 ,len(arr)):
# #             if arr[i] == arr[j] :
# #                 seen -= 1
# #     return seen


# # arr = [22 , 22 , 43 , 24 ,25]

# # result = find_dublicates(arr)

# # print(result)


# # arr = []
# # size_of_array =  int(input("Enter the size of array : "))
# # sum1 = 0
# # print("Enter the elements : ")
# # for i in range(size_of_array):
# #     num = int(input())
# #     arr.append(num)
# # for i in range(0 , size_of_array) :
# #   sum1 += arr[i]
# # print(arr)
# # print("\nThe sum of arrey elements is " , sum1)

# # arr = [12 ,89, 23, 76,45 ,89]
# # for i in range(len(arr)) :
# #     for j in range(i + 1 , len(arr)):
# #         if arr[i] > arr[j] :
# #             arr[i] , arr[j] = arr[j] , arr[i]
# # print(arr)



# # largest = arr[-1]
# # second_largest = None
# # for i in range(len(arr) -2 , -1 , -1):
# #     if arr[i] != largest :
# #         second_largest = arr[i]
# #         break
    
# # if second_largest is not None:
# #     print("This is a second largest number" , second_largest )
        
# arr = [12 ,89, 23, 76,45 ,89]
# count = 0 
# for i in range(len(arr)) :
#     for j in range(i + 1 , len(arr)):
#         if arr[i] > arr[j] :
#             arr[i] , arr[j] = arr[j] , arr[i]



# s1 = "programming"        
# freq = {}

# for char in s1 :
#     if char in freq :
#         freq[char] += 1
        
#     else:
#         freq[char] = 1
# print(freq)     


# string = "Education"
# vowels = "aeiouAEIOU"
# vowels_count = 0
# cons_count = 0
# for char in string :
#     if char.isalpha():
#         if char in vowels :
#             vowels_count += 1
#         else:
#             cons_count += 1


# print("vowels in string are : ", vowels_count)
# print("constant in string are : " , cons_count)



# string = "programming"
# s2 = ""

# for char in string :
#     if char not in s2 :
#         s2 += char
        
# print(s2)
        
# s1 = "listen" 
# s2 = "silent" 

# if len(s1) != len(s2) :
#     print("Not anagram")

# s1_list = list(s1)
# s2_list = list(s2)


# for i in range(len(s1_list)):
#     for j in range(i + 1 , len(s1_list)):
#         if s1_list[i] > s1_list[j] :
#             s1_list[i] , s1_list[j] = s1_list[j] , s1_list[i] 
# print(s1_list)



# for i in range(len(s2_list)):
#     for j in range(i + 1  , len(s2_list)):
#         if s2_list[i] > s2_list[j] :
#             s2_list[i] , s2_list[j] = s2_list[j] , s2_list[i] 
            
# print(s2_list)

# if s1_list == s2_list :
#     print("\nThe string is anagram")
    
# else:
#     print("\nThe string is not anagram")


        
# string = "this is a test this is only a test"
# word = ""
# unique = []
# result = ""
# freq ={}
# for char in string :
#     if char != " " :
#         word += char
#     else:
#         if word not in unique :
#             unique.append(word)
#             result += word + " "
#         word =""
        
# if word not in unique :
#     unique.append(word)
#     result += word
    
# print(result)

# string = "aabbcccdd"

# compress = "" 
# count = 0

# for i in range(1 , len(string)):
#     if string[i] == string[i - 1]:
#         count += 1
        
#     else:
#         compress += string[i - 1] + str(count)
#         count = 1
        
# compress += string[- 1] + str(count)

# print(compress)


# string = "the quick brown fox jumps over the lazy dog"

# alpha = "abcdefghijklmnopqrstuvwxyz"
# count = 0

# for ch in alpha:
#     if ch in string :
#         count += 1
# if count == 26:
#     print("The string is pangram")
    
# else:
#     print("The string is not pangram")


# def get_rate_by_quality(quality):
#     if quality == "basic":
#         return 1200
#     elif quality == "standard":
#         return 1600
#     elif quality == "premium":
#         return 2000
#     else:
#         return None

# area = float(input("Enter area in square feet (per floor): "))
# floors = int(input("Enter number of floors: "))
# quality = input("Enter construction quality (basic / standard / premium): ").lower()

# rate = get_rate_by_quality(quality)

# if rate is None:
#     print("Invalid quality selected.")
# else:
#     total_sqft = area * floors
#     total_cost = total_sqft * rate

#     print(f"\nTotal Construction Area: {total_sqft} sq.ft")
#     print(f"Estimated Rate: ₹{rate}/sq.ft")
#     print(f"Estimated Construction Cost: ₹{total_cost:,.2f}")


# rows = int(input("Enter the number :"))

# for i in range(1 ,rows + 1) :
#     for j in range(rows - i) :
#         print("  " , end = "")
#     for k in range(1 , i + 1) :
#         print(k , end=" ")
#     print()



# # date = 18 / 07 / 2025


# nums = [100, 4, 200, 5, 3, 2, 25,26, 30, 29,33,27] 
# for i in range(1 , len(nums)):
#     key = nums[i]
#     j = i - 1
    
    
#     while j >= 0  and nums[j] > key :
#         nums[j + 1] = nums[j]
        
#         j -= 1
        
#     nums[j + 1] = key
    
    
# print(nums)

# nums = [100, 4, 200, 5, 3, 2, 25,26, 30, 29,33,27] 
# n = len(nums)

# for i in range(n) :
#     min_index = i 
    
#     for j in range(i + 1 , n):
#         if nums[j]  < nums[min_index] :
#             min_index = j
            
            
#     nums[i] , nums[min_index] = nums[min_index] , nums[i]
    
# print(nums)
        
        
# def quick_sort(arr) :
#     if len(arr) <= 1 :
#         return arr
        
#     pivot = arr[0]
#     left = []
#     right = []
    
#     for i in range(1 , len(arr)):
#         if arr[i] < pivot :
#             left.append(arr[i])
            
#         else:
#             right.append(arr[i])
            
#     return quick_sort(left) + [pivot] + quick_sort(right)
    
# nums = [100, 4, 200, 5, 3, 2, 25,26, 30, 29,33,27] 
# print(quick_sort(nums))

# import random 

# otp = ""

# for i in range(6):
#     otp += str(random.randint(0 , 9 ))

# print(otp)

# s = "geekforgeeks"        23 july 2025 question
# s1 = ""

# for i in range(len(s)):
#     s2 = ""
#     for j in range(i + 1 , len(s)):
#         if s[j] in s2 :
#             break
#         s2 += s[j] 
#         if len(s1) < len(s2):
#             s1 = s2 
# print(s1)
        
             
             
# s = "geekforgeeks"  2nd type
# s1 =""
# count = 0
# for ch in s :
#     if ch not in s1:
#         s1 += ch
#         count += 1
# print(count)
# print(s1)


# file = open("linked.py" , "r")
# print(file.read())
# file.close

# from functools import reduce 

# square = lambda x : x * x

# print(reduce(lambda x , y : x * y , map(square , range(1 , 4))))


            # 23 july 2025 algorithms 

# def bubble_sort(arr) :    
#     for i in range(len(arr)):
#         for j in range(i + 1 , len(arr)):
#             if arr[i] > arr[j] :
#                 arr[i] , arr[j] = arr[j] , arr[i] 
                
# arr = [23 , 53 , 64 ,21 , 3]
# bubble_sort(arr)

# print(arr)


# def insertion_sort(arr):
#     for i in range(len(arr)):
#         key = arr[i] 
#         j = i - 1
        
#         while j >= 0  and arr[j] > key :
#             arr[j + 1] = arr[j] 
#             j -= 1
            
            
#         arr[j + 1] = key
        
# arr = [23 , 53 , 64 ,21 , 3]
# insertion_sort(arr)

# print(arr)

# string = "Python is a powerful programming language"
# word = ""
# longest = ""
# max_lenght = 0


# for ch in string:
#     if ch != " ":
#         word += ch
#     else:
#         if len(word) > max_lenght :
#             longest = word
#             max_lenght = len(word)
            
#         word = ""
        
# if len(word) > max_lenght :
#     longest = word 
#     max_lenght = len(word)
    
# print("lenght word : " , max_lenght)

# print("longest word : " , longest)

# string = "Python is a powerful programming language"
# word = "" 
# freq = {} 
# for ch in string :
#     if ch != " ":
#         word += ch
#     else:
#         if word in freq :
#             freq[word] += 1
#         else:
#             freq[word] = 1
#         word = ""
# if word:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)

# nums = [100, 4, 200, 5, 3, 2, 25,26, 30, 29,33,27]

# for i in range(len(nums)):
# 	for j in range(i + 1 , len(nums)):
# 		if nums[i] > nums[j] :
# 			nums[i] , nums[j] = nums[j] , nums[i]
			
# print(nums)

# current = 1 
# max_no = 1
# for i in range( 1 , len(nums)):
# 	if nums[i] == nums[i - 1]:
# 		pass
		
# 	elif nums[i] == nums[i - 1] + 1:
# 		current += 1
		
# 	else:
# 		if current > max_no :
# 			max_no = current 
			
# 		current = 1
		
# 	if current > max_no:
# 		max_no  = current
		
		
# print(max_no)
        

# def merge_sort(arr) :
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
        
        
#         merge_sort(left)
#         merge_sort(right)
        
#         i = j = k = 0 
        
#         while i < len(left) and j < len(right):
#             if arr[i] < arr[j] :
#                 arr[k] = arr[left] 
#                 i += 1
                
#             else:
#                 arr[k] = arr[right]
#                 j += 1
                
#             k += 1
            
            
#         while i < len(left) :
#             arr[k] = left[i] 
#             i += 1
#             k += 1
            
        
#         while j < len(right):
#             arr[k] = right[j] 
#             j += 1
#             k += 1
#     return arr
    
# arr = [34 , 53 , 23 ,73 , 2]
# merge_sort(arr)

# print(arr)



                # 24 July 2025
# num = 18
# original = num
# sum1 = 0 

# while num > 0 :
#     digit = num % 10 
#     sum1 += digit
#     num = num // 10
    
# if original % sum1 == 0 :
#     print("This is harshad number")

# else:
#     print("This is not a harshad number")
    
    

# num =  153
# original = num
# sum1 = 0
# cube = 0

# while num > 0 :
#     digit = num % 10 
#     cube = digit ** 3
#     sum1 += cube
#     num = num //10
    
# if original == sum1:
#     print("This is the armstrong number")
# else:
#     print("This is not armstrong number")
  
  
    
# num = 121
# original = num 
# reverse = 0 

# while num > 0 :
#     digit = num % 10 
#     reverse = reverse * 10 + digit 
#     num = num // 10
    
# if original == reverse:
#     print("The number is palindrome")
    
# else:
#     print("The number is not palindrome")


# num = 9
# sum1 = 0
# original = num 
# square = num * num
# while square > 0 :
#     digit = square % 10
#     sum1 += digit
#     square = square // 10
   
# if sum1 == original:
#     print("This is the neon number")
# else:
#     print("This is not neon number")



# num = 76
# original = num
# square = num * num 
# last = 0
# while square > 0 :
#     digit = square % 10
#     last = square % 100
#     square = square // 10 
    
# if original == last:
#     print("yes")



    
# arr= [12 , 5 ,23 ,433 ,13 ,43]

# first = second = float('-inf' )

# for num in arr :
#     if num > first :
#         second = first
#         first = num
        
        
#     elif num > second and num != first :
#         second = num
        
# print("This is the second largest number" , second)




# a = 10
# b = 20 

# while b != 0 :
#     a , b = b , a % b
    
# print("Gcd is" , a)


# a = 10 
# b = 20 

# x , y =  a , b

# while  y != 0 :
#     x , y = y , x % y 
    
# gcd = x


# lcm = (a * b) // gcd

# print(lcm)




# def merge_arr(list1 , list2):
#     i = 0 
#     j = 0 
#     merge = []
    
#     while i <  len(list1) and j  <  len(list2):
#         if list1[i] < list2[j]:
#             merge.append(list1[i])
#             i += 1
            
#         else:
#             merge.append(list2[j])
#             j += 1
            
#     while i < len(list1):
#         merge.append(list1[i])
#         i += 1
        
#     while j < len(list2):
#         merge.append(list2[j])
#         j += 1
        
#     return merge
    
    
# a = [ 4 , 1 , 3 , 2]
# b = [6 , 8 , 5 , 7]

# print(merge_arr([ 4 , 1 , 3 , 2] ,[6 , 8 , 5 , 7]))




# def rotate_arr(arr , k) :
#     n = len(arr)
#     k = k % n
#     result = []

#     for i in range(k , n ):
#         result.append(arr[i])
        
#     for i in range(0 , k):
#         result.append(arr[i])
        
        
#     return result
    
# arr = [1 , 2 , 3 ,4 ,5]
# k = 3
# rotate = rotate_arr(arr , k)

# print(rotate)




# num = [12, 345, 2, 6, 7896, 676761]
# digit_count = 0
# for i in num:
#     temp = i 
#     digit = 0
#     while temp > 0 :
#         temp = temp // 10
#         digit += 1
        
#     if digit % 2 == 0 :
#         digit_count += 1
        
# print(digit_count)





# nums = [23, 45, 66, 13, 24]

# even_count = 0
# for i in nums :
#     temp = i 
#     sum1 = 0 
    
#     while temp > 0 :
#         digit = temp % 10 
#         sum1 += digit
#         temp = temp // 10
        
#     if sum1 % 2 == 0 :
#         even_count += 1
 
# print(even_count)



# nums = [121, 345, 33, 45654, 789]

# palindrome_count = 0
# for i in nums :
#     temp = i
#     original = temp
#     reverse = 0 
    
#     while temp > 0 :
#         digit = temp % 10 
#         reverse = reverse * 10 + digit 
#         temp = temp // 10 
#     if original == reverse :
#         palindrome_count += 1
        
# print(palindrome_count)
        
        
              
# nums = [153, 370, 9474, 123, 10, 407]

# armstrong_count = 0

# for i in nums :
#     temp = i 
#     original = i
    
#     digit_count = 0 
#     while temp > 0 :
#         digit_count += 1
#         temp = temp // 10
    
#     temp = original 
#     sum1 = 0
#     while temp > 0 :
#         digit = temp % 10
#         power = 1
#         for i in range(digit_count):  # Raise to digit_count power
#             power *= digit
#         sum1 += power
#         temp = temp // 10
        
#     if original == sum1 :
#         armstrong_count += 1
        
        
# print(armstrong_count)
        
        
# nums = [153, 370, 371, 123, 10, 407]

# armstrong_count = 0

# for i in nums :
#     temp = i 
#     original = temp 
#     cube = 0 
#     sum1 = 0
    
#     while temp > 0 :
#         digit = temp % 10 
#         cube = digit ** 3
#         sum1 += cube 
#         temp = temp // 10
        
#     if original == sum1 :
#         armstrong_count += 1
        
# print(armstrong_count)



# s1 = "madam" 
# original = s1
# reverse = ""

# for ch in s1:
#     reverse = ch + reverse
    

# if original == reverse:
#     print("This is palindrome string")
    
# else:
#     print("This is not palindrome string")
    
    
    
# string = "yash"
# vowel = "aeiouAEIOU"

# vowel_count = 0
# const = 0 


# for ch in string:
#     if ch in vowel:
#         vowel_count += 1
        
#     elif ch.isalpha():
#         const += 1
        
#     else:
#         print("Error")

# print(vowel_count) 
# print(const)



# s1 = "yash" 
# s2 = "shelar"


# s1_list = list(s1)
# s2_list = list(s2)


# if len(s2_list) != len(s1_list):
#     print("no")
    
    
# for i in range(len(s1_list)):
#     for j in range(i + 1 , len(s1_list)):
#         if s1_list[i] > s1_list[j] :
#             s1_list[i] , s1_list[j] = s1_list[j] , s1_list[i]
            
# print(s1_list)

# for i in range(len(s2_list)):
#     for j in range(i + 1 , len(s2_list)):
#         if s2_list[i] > s2_list[j] :
#             s2_list[i] , s2_list[j] = s2_list[j] , s2_list[i]
            
# print(s2_list)


# if s1_list == s2_list:
#     print("anagram")
    
# else:
#     print("No anagram")

  
# s = "programming"
# freq = {}
 
# for ch in s :
#     if ch in freq :
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
    
# for ch in freq :
#     if freq[ch] > 1:
#         print(freq[ch])
         
         
         
# s ="programming" 
# unique = ""
# count = 0
# for ch in s: 
#     if ch not in unique :
#         unique += ch
#         count += 1
        
# print(unique)
# print(count)



# s = "programming"


# freq = {}

# for ch in s :
#     if ch in freq:
#         freq[ch] += 1
        
#     else:
#         freq[ch] = 1
        
        
# for ch in freq :
#     if freq[ch] == 1:
#         print("non repeting  charcter" , ch)



# def binery_search(arr , target) :
#     low = 0 
#     high = len(arr) - 1
     
#     while low <= high :
#         mid = (low + high) // 2
        
        
#         if arr[mid] == target :
#             return mid
            
#         elif arr[mid] < target :
#             low = mid + 1
            
#         else:
#             high = mid - 1
#     return -1

# arr = [4,5,6,7,0,1,2]
# target = 0
# result = binery_search(arr , target)

# print(result)



# num = 19 
# square = 0 
# sum1 = 0

# while num > 0 :
#     digit = num % 10 
#     square = digit ** 2
#     sum1 += square
#     num = num // 10
        
# print(sum1)




# arr = [4, 5, 2, 10, 8]
# n = len(arr)

# result = []

# for i in range(n) :
#     next_greater = -1
#     for j in range(i + 1 , n):
#         if arr[i] < arr[j] :
#             next_greater = arr[j] 
#             break
#     result.append(next_greater)
        
# print(result)



# s = "abbaca"
# stack = []
# for ch in s :
#     if stack and stack[-1] == ch:
#         stack.pop()
        
#     else:
#         stack.append(ch)

# result = ''.join(stack)

# print(result)




# arr = [ 5 , 2 , 1 ,4 ,3]    

# for i in range(len(arr)):
#     min_index = i 
#     for j in range(i + 1 , len(arr)):
#         if arr[j] < arr[min_index] :
#             min_index = j 
            
            
#     arr[i] , arr[min_index] = arr[min_index] , arr[i]
    
# print(arr)



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]    
#     left = [x for x in arr[1:] if x < pivot]
#     right = [x for x in arr[1:] if x >= pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)
# arr = [ 5 , 2 , 1 ,4 ,3]  
# result = quick_sort(arr)
# print(result)

