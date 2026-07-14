# Loan Approval Program with Loan Amount Calculation

salary = float(input("Enter your monthly salary (in INR): "))

print("\n--- Loan Approval Status ---")

if salary >= 50000:
    max_loan = salary * 10
    print("Loan Approved: Eligible for high amount.")
    print(f"Maximum Loan Amount: ₹{max_loan:,.2f}")
elif salary >= 30000:
    max_loan = salary * 8
    print("Loan Approved: Eligible for medium amount.")
    print(f"Maximum Loan Amount: ₹{max_loan:,.2f}")
elif salary >= 15000:
    max_loan = salary * 5
    print("Loan Approved: Eligible for small amount.")
    print(f"Maximum Loan Amount: ₹{max_loan:,.2f}")
else:
    print("Loan Not Approved: Salary too low.")
