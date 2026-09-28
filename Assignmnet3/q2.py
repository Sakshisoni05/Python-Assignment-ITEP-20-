# 2.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("Enter quantity : "))
cost = quantity*100
discount=0
if cost > 1000:
    discount = cost * 10/100
    final_cost = cost - discount 

print(f"cost of purchased quantity = {cost}")
print(f"Discount = {discount}")
print(f"total cost = {final_cost}")
