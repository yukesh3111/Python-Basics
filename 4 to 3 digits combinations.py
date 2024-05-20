num=list("6952")
for i in num:
    for j in num:
        for k in num:
            if(int(i)!=int(j) and int(j)!=int(k) and int(k)!=int(i)):
                if(k=="5"):
                    print(i,j,k)
