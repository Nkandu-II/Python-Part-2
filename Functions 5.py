#Create a function random_list_summer creates n elemented list with min value = -100 max value = 100 
#it has to print the list first and sum all the elements of it default element number is 15

import random

def random_list_summer():
    list_of_numbers = []
    limit = 0
    
    while limit <= 15:
        i = random.randint(-100, 100)
        list_of_numbers.append(i)
        limit = limit + 1
        continue
    return print(f' List of numbers : {list_of_numbers}\n The sum of all the numbers above is: {sum(list_of_numbers)}')
random_list_summer()
