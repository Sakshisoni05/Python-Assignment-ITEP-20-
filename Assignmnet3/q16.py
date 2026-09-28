# 16. Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.          Calculate percentage and grade according to following: 
# 	Percentage >= 90% : Grade A 
# 	Percentage >= 80% : Grade B 
# 	Percentage >= 70% : Grade C 
# 	Percentage >= 60% : Grade D 
# 	Percentage >= 40% : Grade E 
# 	Percentage < 40% : Grade F

maths= int(input("enter marks of maths : "))
hindi= int(input("enter marks of hindi : "))
english= int(input("enter marks of english: "))
chemistry= int(input("enter marks of chemistry : "))
physics= int(input("enter marks of physics : "))

per= (maths + hindi + english + chemistry + physics )/5
print("Percentage = ",per)
if per >=90:
    print("GRADE A")
elif per >=80:
    print("Grade B")    
elif per >=70:
    print("Grade C")    
elif per >=60:
    print("Grade D")
elif per >=40 :
    print("GRADE E")    
else:
    print("Grade f")        
