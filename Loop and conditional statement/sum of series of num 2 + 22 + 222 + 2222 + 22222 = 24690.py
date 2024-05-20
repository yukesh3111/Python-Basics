num=2
limit=5
string=""
list1=[]
for i in range(1,limit+1):
    for j in range(i,1+limit):
        string+=str(num)
    list1.append(int(string))
    string=""
print(sum(list1))
