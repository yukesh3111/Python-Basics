def even(a,b):
    list1=[]
    for i in range(a,b+1):
        if(i%2==0):
            list1.append(i)
    return list1  
print(even(0,40))
