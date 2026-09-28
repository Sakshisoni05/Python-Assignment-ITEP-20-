# 7. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# 8. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

class_held = int(input("Number of classes held : "))
class_attended = int(input("Number of classes attended : "))
medical_cause = input("Do you have a medical cause? (Y/N): ")

attendance_percentage = (class_attended / class_held) * 100

print(f"Percentage of class attended: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    if medical_cause == 'y':
        print("Student is allowed to sit in the exam (medical cause).")
    else:
        print("Student is not allowed to sit in the exam.")

