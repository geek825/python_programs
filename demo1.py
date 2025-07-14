def unique_num(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False 
    
print(unique_num([1,2,3,4,5,6]))
print(unique_num([1,2,2,3,4,5,]))