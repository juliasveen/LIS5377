def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Julia Sveen")
    print("Annual Compound Interest Investment Report.")
    print("\nProgram Requirements:\n"
          + "1. Write a program that prints a yearly compound interest report table.\n"
          + "2. Must perform data validation.\n")
    
    print("***Resource(s):***\n"
          + "https://www.fool.com/saving/how-often-is-interest-accrued-on-a-savings-account.aspx\n"
          + "https://www.nerdwallet.com/article/banking/how-to-calculate-interest-in-a-savings-account\n"
          + "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator\n")
    print("Input:")

def get_principal():
    """Prompts for principal amount, returns user-entered value. With data validation!"""
    while True:
        try:
            # prompt initial investment amount
            principal = float(input("Enter principal: $"))
            
            is_within_range = False
            while not is_within_range:
                if principal >= 1 and principal <= 1000000:
                    is_within_range = True
                else:
                    print("Principal must be between $1 and $1,000,000.\n")
                    principal = float(input("Enter principal: $"))
            
            return principal
        except ValueError:
            print("Not a float! Try again.\n")
            continue

def get_rate():
    """Prompts for interest rate, returns user-entered value. With data validation!"""
    while True:
        try:
            # prompt interest rate
            rate = float(input("Enter rate (%): "))
            
            is_within_range = False
            while not is_within_range:
                if rate >= 1 and rate <= 10:
                    is_within_range = True
                else:
                    print("Rate must be between 1% and 10% (no percent sign!).\n")
                    rate = float(input("Enter rate (%): "))
            
            return rate
        except ValueError:
            print("Not a float! Try again.\n")
            continue

def get_years():
    """Prompts for number of years, returns user-entered value. With data validation!"""
    while True:
        try:
            # prompt investment years
            years = int(input("Enter years: "))
            
            is_within_range = False
            while not is_within_range:
                if years >= 1 and years <= 50:
                    is_within_range = True
                else:
                    print("Years must be between 1 and 50.\n")
                    years = int(input("Enter years: "))
            
            return years
        except ValueError:
            print("Not an int! Try again.\n")
            continue

def calculate_interest(principal, rate, years):
    total_interest = 0.0 # initialize accumulator
    rate = rate / 100    # convert rate to decimal value
    
    print() # vertical space
    
    # display table header
    print("{0:<4s} {1:>12s} {2:>12s} {3:>12s}".format("Year", "Starting", "Interest", "Ending"))
    
    # compute and display yearly results
    for year in range(1, years + 1):
        interest = principal * rate
        end_principal = principal + interest
        
        print("{0:>4d} {1:>12,.2f} {2:>12,.2f} {3:>12,.2f}".format(year, principal, interest, end_principal))
        
        principal = end_principal
        total_interest += interest
        
    # display totals
    print("\nEnding principal: ${0:,.2f}".format(principal))
    print("Total interest earned: ${0:,.2f}".format(total_interest))