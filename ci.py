def calculate_compound_interest(principal,rate,time):
    """
    calculate the compound interest.
    :param principal:The initial amount of money(float or int).
    :param rate:The annuual interest for(float or int).
    :return:The compound interest(float).
    """
    #Convert rate from percentage to decimal
    rate_decimal=rate/100
    #calculate the compound interest
    amount=principal*(1+rate_decimal)**time
    compound_interest=amount-principal
    return compound_interest
#input values
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the annual interest rate(in percentage):"))
time=float(input("Enter the number of periods:"))
#calculate compound interest
interest=calculate_compound_interest(principal,rate,time)
#Output the result
print(f"The compound interest is:{interest:.2f}")
