my_dict={'data1':100,'data2':-54,'data3':247}
sum=0
for i in my_dict.values():
    sum+=i
print(f"the sum of all items will be:{sum}")


#or we can use following function
lsit=my_dict.values()
print(sum(lsit))
