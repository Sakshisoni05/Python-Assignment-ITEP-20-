# 5.Take input of age of 3 people by user and determine oldest and youngest among them.

person1 = int(input("Enter age of person 1 : "))

person2 = int(input("Enter age of person 2 : "))

person3 = int(input("Enter age of person 3 : "))

if person1 > person2 and person1 > person3:
    print("Person 1 is elder among three ...")

elif person2 > person1 and person2 > person3:
    print("person 2 is elder among them... ")

else:
    print("person 3 is elder among them .. ")
    