#idk what this shit is its so hard
def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10

print(num()) #num function will now always output 400 because the decorators changed the behavior of the function

#this calls the decorators in this order: decor1(decor(num()))



