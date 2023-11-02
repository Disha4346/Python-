"""gym_members=['april','john','corey']
developers=['judy','corey','steven','jane','april']
set1=set(gym_members)
set2=set(developers)
print(set1.intersection(set2))


s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
s4=s1.difference(s2,s3)
print(s4)
s4=s2.symmetric_difference(s1)
print(s4)"""

students={"name":"alice",
          "age":25,
          "grade":"A"}
"""print(students.get("name"))
print(students.get("age"))
print(students.get("grade"))
a=students.get("kjhg")
print(a)
for key,value in students.items():
    print(f"{key}:{value}")

squares={num:num**3 for num in range(1,6)}
print(squares)"""


del students["grade"]
print(students)









