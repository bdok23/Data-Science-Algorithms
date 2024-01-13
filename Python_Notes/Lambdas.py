def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)
mytripler = my_func(3)

print(mydoubler(11))
print(mytripler(11))


"""
l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))
"""