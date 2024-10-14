company_name = input("Company Name: ")
daily_revenue = int(input("Daily Revenue: "))
daily_expenses = int(input("Daily Expenses: "))
daily_profit = daily_revenue - daily_expenses
daily_profit_margin = daily_profit / daily_revenue
lucrative = (daily_profit_margin >= 0.75)
made_profit = (daily_revenue > daily_expenses)
if (lucrative == True):
     print(company_name, "was lucrative today")
elif (made_profit == True):
    print(company_name, "made a profit today")
else:
    print(company_name, "did not make a profit today")
print("Daily Revenue: £" + str(daily_revenue))
print("Daily Expenses: £" + str(daily_expenses))
print("Daily Profit: £" + str(daily_profit))
print("Daily Profit Margin: " + str(daily_profit_margin))