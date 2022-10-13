str1=input("Enter first string:")
str2=input("enter second string:")
set1=set(str1)
set2=set(str2)
matched=set1 & set2
print("the number of same characters are:",len(matched))