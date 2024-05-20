def divsor(a):
    divsor=[]
    for i in range(1,a):
        if(a%i==0):
            divsor.append(i)
    return divsor
num1=37
num2=60
common=[]
divsor1=divsor(num1)
divsor2=divsor(num2)
maxnum1=max(divsor1)
maxnum2=max(divsor2)
for i in reversed(divsor1):
    for j in reversed(divsor2):
        if(i==j):
            common.append(i)
print(max(common))

