list1=[10,5,15,40,50,80,100]
def total():
    sum=0
    for i in list1:
        sum=sum+i
    print("total sum is:",sum)
def maxi():
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    print("maximum is:",max)
def mini():
    Mini = list1[0]
    for i in list1:
        if i < Mini:
            Mini = i
    print("minimum is:",Mini)
total()
maxi()
mini()