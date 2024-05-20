num=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(num)):
    for j in range(2,num[i]-1):
        if(num[i]%j==0):
            print(num[i],"is not a prime number")
            break
    else:
        print(i,"is prime number")
