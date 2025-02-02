def calculate_tax(salary):
    standard_deduction = 75000
    taxable_income = max(0, salary - standard_deduction)  # Ensure tax is not negative
    tax = 0

    tax_slabs = [
        (400000, 0.00),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
        (float('inf'), 0.30),
    ]

    previous_limit = 0

    for limit, rate in tax_slabs:
        if taxable_income > previous_limit:
            taxable_amount = min(taxable_income, limit) - previous_limit
            tax += taxable_amount * rate
            previous_limit = limit
        else:
            break

    return tax

# Example usage
salary = float(input("Enter your annual salary: ₹"))
tax = calculate_tax(salary)
print(f"Total tax to be deducted: ₹{tax:,.2f}")
print(f"Net salary after tax: ₹{salary - tax:,.2f}")
