# common prefix


list1 = ["yash", "yamini" , "yahoo"]
prefix = ""
first = list1[0]

for i in range(len(first)):
    char = first[i]
    for word in list1:
        if i >= len(word) or word[i] != char:
            print("common prefix", prefix)

            exit()
    prefix += char
print("common prefix is" , prefix)
