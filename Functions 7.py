# Create a lambda function that returns 2nd power of given number if its even
# and run it on the given list
# then print the result to the screen

list_of_even_numbers = []

for i in range(10):
    if i%2 == 0:
        x = lambda i : i**2
        list_of_even_numbers.append(i)
        print(list_of_even_numbers)
        print(x(i))
    else:
        pass