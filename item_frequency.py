array=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
dict={}
for item in array:
    if item not in dict.keys():
        dict[item]=1
    elif item in dict.keys():
        dict[item]=dict[item]+1 # hash function
print(dict)