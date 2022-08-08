def agerfilter():
    list1 = [{'name': 'prabhat', 'Age': 22},
             {'name': 'anu didi', 'Age': 21},
             {'name': 'nitesh', 'Age': 20}]
    global a
    a = []
    for d in list1:
        if d['Age'] > 20:
            a.append(d)
    print(a)


def print_name():
    x = []
    for b in a:
        c = b['name']
        x.append(c)
    x.sort()
    for j in x:
        print(j)

agerfilter()
print_name()


