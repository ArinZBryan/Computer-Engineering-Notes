def print_money(value):
    if (value < 0):
        return "-£" + str(abs(value))
    else:
        return "£" + str(abs(value))

company_name = input("Company Name: ")

weekly_revenue = 0
weekly_expenses = 0
most_profit = 0
most_profit_day = 0
most_expensive = 0
most_expensive_day = 0

for day in range(1,8):
    revenue_query = "Daily Revenue " + str(day) + ": "
    expenses_query = "Daily Expenses for day " + str(day) + ": "
    revenue = int(input(revenue_query))
    expenses = int(input(expenses_query))
    weekly_revenue += revenue
    weekly_expenses += expenses
    if (expenses > most_expensive):
        most_expensive = expenses
        most_expensive_day = day
    if (revenue - expenses > most_profit):
        most_profit = revenue - expenses
        most_profit_day = day
    
weekly_profit = weekly_revenue - weekly_expenses
weekly_profit_margin = weekly_profit / weekly_revenue

lucrative = False
if weekly_profit_margin >= 0.75:
    lucrative = True

if lucrative == True:
    print(company_name, "was lucrative this week")
elif weekly_profit > 0 and not lucrative:
    print(company_name, "made a profit this week")
elif weekly_profit <= 0:
    print(company_name, "did not make a profit this week")
print("Weekly Revenue: " + print_money(weekly_revenue))
print("Weekly Expenses: " + print_money(weekly_expenses))
print("Weekly Profit: " + print_money(weekly_profit))
print("Weekly Profit Margin: " + str(weekly_profit_margin))
print("Most Profitable Day: " + str(most_profit_day))
print("Most Expensive Day: " + str(most_expensive_day))
