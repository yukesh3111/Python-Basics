n=int(input())
sets=set(map(int,input().split()))
count=int(input())
for i in range(count):
    string_list=input().split()
    if("pop" in string_list):
        sets.pop()
    if("remove" in string_list):
        num=int(string_list[1])
        sets.remove(num)
    if("discard" in string_list):
        num=int(string_list[1])
        sets.discard(num)
print(sum(sets))
