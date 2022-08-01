a = int(input("enter a number:"))
sum=0
print("even factors of", a, "are:")
for i in range (1,a+1):
    if a%i == 0:
        if i%2 ==0:
            print(i)
            sum=sum+i
print("sum of even factors is=", sum)
