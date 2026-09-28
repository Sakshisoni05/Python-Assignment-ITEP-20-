name = input("Enter your name: ")
gender = input("Enter your gender: ")

# ---------------- ITEM 1 ----------------
item1 = input("What is your 1st item: ")
quantity1 = int(input(f"Enter quantity of your {item1}: "))
p1 = 10
price1 = p1 * quantity1

if quantity1 > 4:
    discount1 = price1 * 5 / 100
else:
    discount1 = 0

final_price1 = price1 - discount1


# ---------------- ITEM 2 ----------------
item2 = input("Second item: ")
quantity2 = int(input(f"Enter quantity of your {item2}: "))
p2 = 20
price2 = p2 * quantity2
final_price2 = price2


# ---------------- ITEM 3 ----------------
item3 = input("Third item: ")
quantity3 = int(input(f"Enter quantity of your {item3}: "))
p3 = 30
price3 = p3 * quantity3
final_price3 = price3


# ---------------- ITEM 4 ----------------
item4 = input("Fourth item: ")
quantity4 = int(input(f"Enter quantity of your {item4}: "))
p4 = 40
price4 = p4 * quantity4
final_price4 = price4


# ---------------- ITEM 5 ----------------
item5 = input("Fifth item: ")
quantity5 = int(input(f"Enter quantity of your {item5}: "))
p5 = 50
price5 = p5 * quantity5

discount5 = price5 * 10 / 100
final_price5 = price5 - discount5


# ---------------- ITEM 6 ----------------
item6 = input("Sixth item: ")
quantity6 = int(input(f"Quantity of {item6}: "))
p6 = 60
price6 = p6 * quantity6
final_price6 = price6


# ---------------- ITEM 7 ----------------
item7 = input("Seventh item: ")
quantity7 = int(input(f"Quantity of {item7}: "))
p7 = 70
price7 = p7 * quantity7
final_price7 = price7


# ---------------- ITEM 8 ----------------
item8 = input("Eighth item: ")
quantity8 = int(input(f"Quantity of {item8}: "))
p8 = 80
price8 = p8 * quantity8
final_price8 = price8


# ---------------- ITEM 9 ----------------
item9 = input("Ninth item: ")
quantity9 = int(input(f"Quantity of {item9}: "))
p9 = 90
price9 = p9 * quantity9
final_price9 = price9


# ---------------- ITEM 10 ----------------
item10 = input("Tenth item: ")
quantity10 = int(input(f"Quantity of {item10}: "))
p10 = 100
price10 = p10 * quantity10

discount10 = price10 * 15 / 100
final_price10 = price10 - discount10


# ---------------- TOTAL AFTER ITEM DISCOUNTS ----------------

total = (
    final_price1 +
    final_price2 +
    final_price3 +
    final_price4 +
    final_price5 +
    final_price6 +
    final_price7 +
    final_price8 +
    final_price9 +
    final_price10
)


# ---------------- BILL DISCOUNT ----------------

if total > 10000:
    bill_discount = total * 15 / 100

elif total >= 5000:
    bill_discount = total * 10 / 100

else:
    bill_discount = 0

final_total = total - bill_discount

total_discount = bill_discount + discount1+ discount5 + discount10

# ---------------- GST ----------------

gst = final_total * 10 / 100


# ---------------- CARRY BAG ----------------

carry_bag = input("Do you want a carry bag? ")

cb = 0

if carry_bag.lower() == "yes":
    cb = 10


# ---------------- GIFT ----------------

if gender.lower() == "female":
    gift = "Cadbury"

elif gender.lower() == "male":
    gift = "Ledger Wallet"

else:
    gift = "No Gift"


# ---------------- FINAL AMOUNT ----------------

final_amount = final_total + gst + cb


# ---------------- BILL ----------------

print("\n\n\t\tD-MART")
print(f"Name : {name}\t\tDate : 15/09/2026")
print("------------------------------------------------------------")

print("Item Name\tQuantity\tPrice\tTotal\tAfter Discount")

print(f"{item1}\t\t{quantity1}\t\t{p1}\t{price1}\t{final_price1:.2f}")
print(f"{item2}\t\t{quantity2}\t\t{p2}\t{price2}\t{final_price2:.2f}")
print(f"{item3}\t\t{quantity3}\t\t{p3}\t{price3}\t{final_price3:.2f}")
print(f"{item4}\t\t{quantity4}\t\t{p4}\t{price4}\t{final_price4:.2f}")
print(f"{item5}\t\t{quantity5}\t\t{p5}\t{price5}\t{final_price5:.2f}")
print(f"{item6}\t\t{quantity6}\t\t{p6}\t{price6}\t{final_price6:.2f}")
print(f"{item7}\t\t{quantity7}\t\t{p7}\t{price7}\t{final_price7:.2f}")
print(f"{item8}\t\t{quantity8}\t\t{p8}\t{price8}\t{final_price8:.2f}")
print(f"{item9}\t\t{quantity9}\t\t{p9}\t{price9}\t{final_price9:.2f}")
print(f"{item10}\t\t{quantity10}\t\t{p10}\t{price10}\t{final_price10:.2f}")

print("------------------------------------------------------------")

print(f"Original Total : {total} Rs")
print(f"Bill Discount  : {total_discount} Rs")
print(f"After Discount : {final_total} Rs")
print(f"Gift           : {gift}")
print(f"Carry Bag      : {carry_bag}   {cb} Rs")
print(f"GST (10%)      : {gst} Rs")

print("------------------------------------------------------------")
print(f"FINAL AMOUNT   : {final_amount} Rs")
print("------------------------------------------------------------")

print("\n\t\tThank You")
print("\t\tTo Visit")
print("\t\tD-Mart")