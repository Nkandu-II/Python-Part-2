# Implement Fibonacci sequence as recursive function and print first 5 elements.

def the_fibonnaci_sequence():
    n1 = 1
    n2 = 1
    fibonnaci_list = []
    counter = 3
    
    fibonnaci_list.append(n1)
    fibonnaci_list.append(n2)
    
    for i in range(counter):
        new_number = n1 + n2
        n2 = n1
        n1 = new_number
        fibonnaci_list.append(n1)
    return print(fibonnaci_list)

the_fibonnaci_sequence()
