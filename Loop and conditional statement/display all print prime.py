initial=25
final=77
for i in range(initial,final):
    for j in range(2,i-1):
        if(i%j==0):
            break
    else:
        print(i)
