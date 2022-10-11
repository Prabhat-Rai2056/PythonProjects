list1=[10,5,15,40,50,80,100]
def even_odd_func():
    even=[]
    odd=[]
    dict={}
    for i in list1:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    dict["even"]=even
    dict["odd"] =odd
    return dict
print(even_odd_func())



