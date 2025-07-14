def is_anagram(str1 ,str2):
    if len(str1) != len(str2):
        return False
        
    return sorted(str1) == sorted(str2)

s1 = input("Enter the string")
s2 = input("Enter the string")


if is_anagram(s1 , s2):
    print("This is the anagram string")
    
else:
    print("This is not anagram string")