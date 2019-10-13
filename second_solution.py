list1 = eval(input())
k = int(input())
for i in range(len(list1)):
    if i < len(list1)-2:
        s = list1[i] + list1[i+1] + list1[i+2] 
        if s == k:
            print(list1[i],list1[i+1],list1[i+2])