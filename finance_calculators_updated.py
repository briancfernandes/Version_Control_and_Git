# This program enables the user to access two different financial  
# calculators: An investment calculator and a home loan repayment calculator.

import math

# Create functions to check if the input is a valid number (positive  
# float) and prompts the user if not the case.
def is_valid_number(number):
        try: 
           return float(number) > 0
        except ValueError:
           return False      

def get_positive_float(prompt):
        while True:
           number = input(prompt)
           if is_valid_number(number):
              return float(number)
           else:
              print("Invalid input. Please enter a positive number.")

          
# Print initial information for the user and ask for their choice of  
# calculator selection.
print ("investment - to calculate the amount of interest you'll earn on " 
       "your investment \nbond       - to calculate the amount you'll " 
       "have to pay on a home loan \n" )
calculator = input ("Enter either 'investment' or 'bond' from the menu " 
                    "above to proceed: ")

# Ensure that all inputs of the calculator are valid by converting the  
# input to lower case.
calculator = calculator.lower()


# Display an error message if a valid selection isn't made as the else  
# message in the if statement. Calculation based on the investment  
# calculator and whether simple or compound interest is selected.
if calculator == 'investment':
        deposit = get_positive_float("Please enter the amount of money " 
                                     "you are depositing: ")
        interest_rate = get_positive_float("Please enter the interest rate (as"
                                     "a percentage without the % symbol): ")
        years = int(input("Please enter the number of years you plan to invest: "))
        interest = (input("Would you like the calculation to be done based on " 
                          "simple or compound interest? "))
        interest = interest.lower()

        if interest == 'simple':
            amount = int(deposit * (1 + ((interest_rate/100) * years)))
            print(f"the total amount at the end of the period (deposit + interest) " 
                  f"is {amount}")

        elif interest == 'compound':
            amount = int(deposit * math.pow((1 + (interest_rate/100)), years))
            print(f"the total amount at the end of the period (deposit + interest)" 
                  f"is {amount}")

        else:
            print("You have selected an incorrect option!")


# Calculation based on the bond calculator.
elif calculator == 'bond':
        house_price = get_positive_float("Enter the present value of the house: ")
        interest_ratebond = get_positive_float("Enter the interest rate (as a"
                                         " percentage without the % symbol): ")
        loan_term_years = int(input("Enter the loan term (in years): "))
        months = loan_term_years * 12

        # Down payment amount (optional)
        down_payment = get_positive_float("Enter the down payment amount (optional, "
                                          "0 for no down payment): ")

        # Loan amount after down payment
        loan_amount = house_price - down_payment

        # Error handling to ensure loan amount is positive
        if loan_amount <= 0:
              print("Error: Loan amount cannot be zero or negative.")
              exit()   

        monthly_interest = (interest_ratebond / 100) / 12
        repayment = (loan_amount * monthly_interest) \
                    / (1 - ((1 + monthly_interest)**(-months)))

        print (f"You will have to repay {repayment:.2f} each month for "
               f"{loan_term_years} years.")

# Response if any other input is made
else:
        print ("You have selected an incorrect option!")