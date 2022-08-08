def Agefilter():
    list1 = [{'name': 'prabhat', 'Age': 22},
             {'name': 'anu didi', 'Age': 21},
             {'name': 'nitesh', 'Age': 20}]

    global a
    a = [d for d in list1 if d['Age'] > 20]
    print("list of name having age greater than 20", a)

def print_ascending():
    b = [m['name'] for m in a]
    b.sort()
    print("Name in ascending order", b)
Agefilter()
print_ascending()