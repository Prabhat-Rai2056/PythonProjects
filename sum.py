list1 = [11, 5, 17, 18, 23]
sum=0
i=0
odd=[]
j=18
for i in list1:
    sum=sum+i
    if i%2!=0:
        odd.append(i)
if j in list1:
    print("yes")
else:
    print("no")
print(sum)
print(min(list1))
print(odd)
print(sorted(list1))
list1.reverse()
print(list1)
list1.remove(5)
print(list1)
print(list1.pop(1))
