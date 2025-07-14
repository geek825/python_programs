# # Top 50 Medium-Level Python Programs (Without Built-in Functions)

# # 1. Check if a number is prime
# num = 29
# is_prime = True
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")

# # 2. Find factorial of a number
# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial:", fact)

# # 3. Check if a number is Armstrong
# num = 153
# sum = 0
# temp = num
# d = 0
# while temp > 0:
#     d += 1
#     temp //= 10
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** d
#     temp //= 10
# if num == sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# # 4. Check palindrome number
# num = 121
# original = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# if original == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # 5. Find GCD of two numbers
# a, b = 60, 48
# while b:
#     a, b = b, a % b
# print("GCD:", a)

# # 6. Find LCM of two numbers
# a, b = 15, 20
# gcd = a
# while b:
#     gcd, b = b, gcd % b
# lcm = (a * 20) // gcd
# print("LCM:", lcm)

# # 7. Fibonacci series upto n terms
# n = 10
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# print()

# # 8. Reverse digits of a number
# num = 1234
# rev = 0
# while num:
#     rev = rev * 10 + num % 10
#     num //= 10
# print("Reversed:", rev)

# # 9. Count digits in number
# num = 123456
# count = 0
# while num:
#     count += 1
#     num //= 10
# print("Digits:", count)

# # 10. Sum of digits
# num = 12345
# sum = 0
# while num:
#     sum += num % 10
#     num //= 10
# print("Sum:", sum)

# # 11. Count vowels and consonants
# s = "helloWorld"
# vowels = "aeiouAEIOU"
# v = c = 0
# for ch in s:
#     if ch.isalpha():
#         if ch in vowels:
#             v += 1
#         else:
#             c += 1
# print("Vowels:", v, "Consonants:", c)

# # 12. Remove vowels from string
# s = "beautiful"
# v = "aeiouAEIOU"
# result = ""
# for ch in s:
#     if ch not in v:
#         result += ch
# print("Without vowels:", result)

# # 13. Check if string is palindrome
# s = "madam"
# rev = ""
# for ch in s:
#     rev = ch + rev
# print("Palindrome" if s == rev else "Not Palindrome")

# # 14. Count frequency of characters
# s = "aabbecc"
# for i in range(len(s)):
#     count = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count += 1
#     found = False
#     for k in range(i):
#         if s[i] == s[k]:
#             found = True
#             break
#     if not found:
#         print(s[i], ":", count)

# # 15. Reverse string without slicing
# s = "hello"
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)

# # 16. Find all prime numbers in range
# n = 50
# for i in range(2, n+1):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i, end=" ")
# print()

# # 17. Swap two variables without temp
# a, b = 5, 10
# a = a + b
# b = a - b
# a = a - b
# print("a:", a, "b:", b)

# # 18. Convert decimal to binary
# num = 10
# binary = ""
# while num > 0:
#     binary = str(num % 2) + binary
#     num //= 2
# print("Binary:", binary)

# # 19. Convert binary to decimal
# binary = "1010"
# decimal = 0
# for i in range(len(binary)):
#     decimal = decimal * 2 + int(binary[i])
# print("Decimal:", decimal)

# # 20. Find power without pow()
# base = 2
# exp = 5
# res = 1
# for _ in range(exp):
#     res *= base
# print("Power:", res)

# # 21. Find second largest number in list
# arr = [10, 20, 4, 45, 99, 99, 45]
# first = second = -1
# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num
# print("Second largest:", second)

# # 22. Remove duplicates from list
# arr = [1, 2, 2, 3, 4, 4, 5]
# unique = []
# for i in arr:
#     if i not in unique:
#         unique.append(i)
# print("Without duplicates:", unique)

# # 23. Reverse a list manually
# arr = [1, 2, 3, 4, 5]
# reversed_arr = []
# for i in range(len(arr)-1, -1, -1):
#     reversed_arr.append(arr[i])
# print("Reversed list:", reversed_arr)

# # 24. Sum of even and odd numbers in list
# arr = [1, 2, 3, 4, 5, 6]
# even_sum = 0
# odd_sum = 0
# for num in arr:
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num
# print("Even sum:", even_sum)
# print("Odd sum:", odd_sum)

# # 25. Merge two lists without using '+'
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# merged = []
# for i in l1:
#     merged.append(i)
# for i in l2:
#     merged.append(i)
# print("Merged list:", merged)

# # 26. Find common elements in two lists
# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]
# common = []
# for i in l1:
#     for j in l2:
#         if i == j and i not in common:
#             common.append(i)
# print("Common elements:", common)

# # 27. Left rotate list by 1
# arr = [1, 2, 3, 4, 5]
# rotated = []
# for i in range(1, len(arr)):
#     rotated.append(arr[i])
# rotated.append(arr[0])
# print("Left rotated:", rotated)

# # 28. Find missing number in list of 1 to N
# arr = [1, 2, 4, 5, 6]
# n = 6
# expected_sum = n * (n + 1) // 2
# actual_sum = 0
# for num in arr:
#     actual_sum += num
# print("Missing number:", expected_sum - actual_sum)

# # 29. Find duplicate elements in list
# arr = [1, 2, 3, 2, 4, 3, 5]
# duplicates = []
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j] and arr[i] not in duplicates:
#             duplicates.append(arr[i])
# print("Duplicates:", duplicates)

# # 30. Count frequency of elements in list
# arr = [1, 2, 2, 3, 3, 3, 4]
# for i in range(len(arr)):
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#     found = False
#     for k in range(i):
#         if arr[i] == arr[k]:
#             found = True
#             break
#     if not found:
#         print(arr[i], ":", count)

# # 31. Number triangle pattern
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# # 32. Floyd’s Triangle
# n = 5
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()

# # 33. Pascal’s Triangle (simplified version)
# n = 5
# for i in range(0, n):
#     num = 1
#     for j in range(0, i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()

# # 34. Diamond Pattern
# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# # 35. Hollow square pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # 36. Right-angled star triangle
# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

# # 37. Inverted number triangle
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# # 38. Zig-zag number pattern
# n = 5
# count = 1
# for i in range(1, n + 1):
#     for j in range(n):
#         print(count, end=" ")
#         count += 1
#     print()

# # 39. Pyramid number pattern
# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# # 40. Continuous number triangle (1 to N)
# n = 5
# count = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()


# def sum_of_prime(n):
#     sum = 0
#     for i in range(2 , n + 1):
#         is_prime = True
#         for j in range(2 , int(i ** 0.5) + 1):
#             if i % j == 0:
#                 is_prime  = False
#                 break

#             if is_prime :
#                 sum += i

#     return sum

# n = int(input("Enter the number :"))

# result = sum_of_prime(n)

            
            



    
    