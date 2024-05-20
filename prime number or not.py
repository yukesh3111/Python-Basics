num=48
for i in range(2,47-1):
    if(num%i==0):
        print(num,"is not a prime number")
        break
else:
    print(num,"is prime number")
