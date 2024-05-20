def linearsearch(list1,target):
    index=""
    for i in range(0,len(list1)):
        if(target==list1[i]):
            index= i
            break
        else:
            index= "Not Found"

    return index
        
            
        
list1=[45,8,9,5,47,58,1,3,54,98]
target=58
print(linearsearch(list1,target))
