d={1:10,2:20,3:30,4:40,5:50,6:60}
x=int(input("enter the number you want to check:"))
if x in d.keys():
    print(f"{x} is in the dictionary.")
else:
    print("it is not in the dictionary.")

