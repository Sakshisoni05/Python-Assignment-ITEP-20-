# 12.A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895 
# without uding loop

num = input("Enter a 4-digit number: ")
rev = 0
num = int(num)
rev = rev * 10 + num % 10
num = num // 10
rev = rev * 10 + num % 10
num = num // 10
rev = rev * 10 + num % 10
num = num // 10
rev = rev * 10 + num % 10
print("Reversed number:", rev)

number = int(input("enter 4 digit number : "))
number = str(number)
print(f'Reversed number is : {number[::-1]}')