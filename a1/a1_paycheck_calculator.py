print("Pay Check Calculator")
print("Program calculates net pay based upon hours worked, hourly rate, and taxes paid.\n")

print("Program Requirements:")
print("Developer: Julia Sveen, BSIT")
print("1. Must use float data type for user input.")
print("2. Must round calculations to two decimal places.")
print("3. Must format currency with dollar sign, and two decimal places.\n")


print("User Input:")
hours_worked = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Rate: $"))
tax_rate = float(input("Tax Rate (percent): "))

print("\nProgram Output:")
gross_pay = hours_worked * hourly_rate
print(f"Gross Pay: ${gross_pay:,.2f}")
print(f"Tax Rate: {tax_rate:,.2f}%")
tax_amt = gross_pay * (tax_rate / 100)
print(f"Tax Amount: ${tax_amt:,.2f}")
net_pay = gross_pay - tax_amt
print(f"Net Pay: ${net_pay:,.2f}")

