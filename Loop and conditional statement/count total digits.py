num=45789
#strnum=str(num)
#listnum=list(strnum)
#print(len(listnum))
i=0
rev=0
while(num!=0):
    i+=1
    rem=num%10
    rev=(rev*10)+rem
    num//=10
    print(num)
print(rev,i)
