person1={
    "Name":"Nitesh",
    "Marks":{
        "Theory":[50,60,70],
        "Practical":[18,19,20]
    }
}
person2={
    "Name":"Prabhat",
    "Marks":{
        "Theory":[55,65,75],
        "Practical":[18,19,20]
    }
}
person3={
    "Name":"Anu didi",
    "Marks":{
        "Theory":[65,75,60],
        "Practical":[18,19,20]
    }
}
def p1():
    new1={}
    sum1=0
    sum2=0
    n=person1["Name"]
    Name= n
    m=person1["Marks"]
    t1 = m["Theory"]
    p1= m["Practical"]
    for i in t1:
        sum1=sum1+i
    for j in p1:
        sum2=sum2+j
    Total= (sum1+sum2)
    percentage = ((sum1+sum2)/3)
    for variable in ["Name", "Total", "percentage"]:
        new1[variable] = eval(variable)
    global l1
    l1 = {}
    l1 = new1
def p2():
    new1={}
    sum1=0
    sum2=0
    n=person2["Name"]
    Name= n
    m=person2["Marks"]
    t1 = m["Theory"]
    p1= m["Practical"]
    for i in t1:
        sum1=sum1+i
    for j in p1:
        sum2=sum2+j
    Total= (sum1+sum2)
    percentage = ((sum1+sum2)/3)
    for variable in ["Name", "Total", "percentage"]:
        new1[variable] = eval(variable)
    global l2
    l2 = {}
    l2=new1
def p3():
    new1={}
    sum1=0
    sum2=0
    n=person3["Name"]
    Name= n
    m=person3["Marks"]
    t1 = m["Theory"]
    p1= m["Practical"]
    for i in t1:
        sum1=sum1+i
    for j in p1:
        sum2=sum2+j
    Total= (sum1+sum2)
    percentage1 = ((sum1+sum2)/3)
    percentage=round(percentage1,2)
    for variable in ["Name", "Total", "percentage"]:
        new1[variable] = eval(variable)
    global l3
    l3 = {}
    l3 = new1
p1()
p2()
p3()
new=[]
new.append(l1)
new.append(l2)
new.append(l3)
print(new)



