mylist=[[1,[{"Name":"Nitesh","Age":20}]],
        [2,[{"Name":"Prabhat","Age":20}]],
        [3,[{"Name":"Anu didi","Age":20}]]]
print("SN \t\t\t Name \t\t\t\t Age")
def display(*args):
    for person in args[0]:
        p=person[1][0]
        print(person[0],"\t\t\t",p["Name"],"\t\t\t",p["Age"])
display(mylist)