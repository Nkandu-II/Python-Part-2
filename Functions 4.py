#Create a function for John Doe and his family that greets every one in the family.

def say_hi_family(*args):
    for i in range(len(args)):
        for j in args[i]: 
            print(f' hello {j}!')
           
say_hi_family(["John Doe", "Tristram Mcbride", "Baldwin Preston", "Wally Collins"])