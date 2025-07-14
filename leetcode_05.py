# Find if Digit Game Can Be Won
    
def Sub():
    count1 = 0
    count2 = 0 
    
    for i  in range(5):
        num = int(input("Enter the number"))
        if num <= 10:
            count1 += num 
        else:
            count2 += num 
    return count1 != count2
result = Sub()

print(result)
