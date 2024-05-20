def recru(n):
    if(n):
        return n+recru(n-1)
    else:
        return 0
print(recru(10))
        
