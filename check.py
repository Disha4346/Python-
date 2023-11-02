"""x=input("enter your name:")
length=len(x)
print(length)
age=int(input("enter your age:"))
if age>=18:
    print("you are an adult.")
else:
    print("you are minor.")

score=85
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("F")

is_raining=True
is_cold=False
if is_raining:
    print("bring an umbrella.")
    if is_cold:
        print("wear a coat")

num=10
if num>0:
    print("number is positive")
elif num<0::
    print("number is negative.")
else:
    print("number is zero.")


tes=set("disha")
print(tes)
tes.add('4')
print(tes)
tes.discard("1")
print(tes)
tes1={1,2,3,1,4}
print(tes.intersection(tes1))"""

def inter_diff(set1,set2):
    inter=set1.intersection(set2)
    diff=set2.difference(set1)
    print( inter)
    print(  diff)

x={"a","b","c","d","f"}
y={"c","e","f","d"}
inter_diff(x,y)



