# 9. Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

char = input("ENTER ANY CHARACTER : ")

if char.islower():
    print(f"The entered character {char} is lowercase.")

if char.isupper():
    print(f"The entered character {char} is uppercase.")

