company_name = input("Company Name: ")
weekly_revenue = 0
weekly_expenses = 0
for day in range(7):
    revenue = int(input("Daily Revenue for day (" + str(day + 1) + "): "))
    expenses = int(input("Daily Expenses for day (" + str(day + 1) + "): "))
    weekly_revenue += revenue
    weekly_expenses += expenses
weekly_profit = weekly_revenue - weekly_expenses
weekly_profit_margin = weekly_profit / weekly_revenue
lucrative = (weekly_profit_margin >= 0.75)
made_profit = (weekly_revenue > weekly_expenses)
if (lucrative == True):
    print(company_name, "was lucrative this week")
elif (weekly_profit > 0):
    print(company_name, "made a profit this week")
else:
    print(company_name, "did not make a profit this week")
print("Weekly Revenue: £" + str(weekly_revenue))
print("Weekly Expenses: £" + str(weekly_expenses))
print("Weekly Profit: £" + str(weekly_profit))
print("Weekly Profit Margin: " + str(weekly_profit_margin))