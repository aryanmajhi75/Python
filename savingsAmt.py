print("Some Calculator!")
rate=float(input("Enter the interest rate :"))
year=int(input("Enter the number of years :"))
principal=float(input("Enter the principal amount :"))

compundInterest=principal*(1.0+(rate/year)**(year*rate));

print("After %d years, the savings will be Rs. %.2f"%(year,compundInterest))