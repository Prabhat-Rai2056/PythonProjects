my_str="egggiggresodsu"
def str():
    vowel=set("aeiou")
    sum=set()
    for i in my_str:
        if i in vowel:
            sum.add(i)
        else:
            pass
    if len(sum) == len(vowel):
        print("accept")
    else:
        print("reject")
str()