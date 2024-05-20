def outer(a,b):
    def inner():
        sums=a+b
        return sums
    return inner()+5
print(outer(5,5))

