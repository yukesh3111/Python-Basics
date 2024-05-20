numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(1,len(numbers),1):
    if(numbers[i]>=500):
        break
    elif(numbers[i]>150):
        i+=1
    elif(numbers[i]%5==0):
        print(numbers[i])
