# Iterate each elements of list1,tuple1,set1 and print them out

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
 
for i in list1:
    print(i,'', end = '')
print()
for j in tuple1:
    print(j,'', end = '')
print()
for k in set1:
    print(k,'', end = '')
print()
for key in dict1:
    if dict1[key] == 'land':
        print(key)
