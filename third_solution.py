def non_dec(list1):
    c = 0
    for i in range(len(list1)):
        if  i<len(list1)-1 and list1[i] < list1[i+1]:
            c += 1
        else:
            pass
    if c ==1:
        return 'True'
    else:
        return 'False'




list1 = list(map(int,input().split()))
s = non_dec(list1)
print(s)