# Student Performance Card

percentage = float(input("Enter your overall percentage: "))

print("\n--- Student Performance Card ---")

if percentage >= 90:
    grade = "A+"
    remark = "Excellent performance!"
elif percentage >= 75:
    grade = "A"
    remark = "Very good, keep it up."
elif percentage >= 60:
    grade = "B"
    remark = "Good, but can improve."
elif percentage >= 45:
    grade = "C"
    remark = "Average, needs more effort."
elif percentage >= 33:
    grade = "D"
    remark = "Pass, but work harder."
else:
    grade = "F"
    remark = "Fail. Better luck next time."

print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print(f"Remarks: {remark}")
