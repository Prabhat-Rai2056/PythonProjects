list= [1, 5, 7, 9, 3, 1, 10, 7, 16, 9]
l1=[]
for i in list:
    if i not in l1:
        l1.append(i)
    else:
        print(i)

