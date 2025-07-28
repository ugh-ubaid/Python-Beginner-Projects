def mortgage_calculator():
    print("Welcome to Mortgage Calculator")
    
    P = float(input("Enter the loan amount (₹): "))
    annual_rate = float(input("Enter the annual interest rate (in %): ")) / 100
    years = int(input("Enter the loan term (in years): "))
    interval = input("Choose compounding interval (monthly/weekly/daily/continuous): ").lower()

    if interval == "monthly":
        r = annual_rate / 12
        n = years * 12
    elif interval == "weekly":
        r = annual_rate / 52
        n = years * 52
    elif interval == "daily":
        r = annual_rate / 365
        n = years * 365
    elif interval == "continuous":
        # Continuous compound uses a different formula (P * e^(rt)), no fixed monthly payment concept
        import math
        total = P * math.exp(annual_rate * years)
        print(f"With continuous compounding, you'll owe ₹{total:.2f} in {years} years.")
        return
    else:
        print("Invalid compounding interval!")
        return

    # Monthly/Weekly/Daily Payments Calculation
    M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    print(f"\nCompounding interval: {interval.capitalize()}")
    print(f"Payment per period: ₹{M:.2f}")
    print(f"Total number of payments: {n}")
    print(f"Total amount paid: ₹{M * n:.2f}")
