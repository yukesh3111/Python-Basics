curent=1
previous=0
temp=0
for i in range(2,11,1):
    sums=curent+previous
    print("current numbere is ",curent,"previous number is ",previous,"= ",sums)
    temp=curent
    previous=curent
    curent=i
    
