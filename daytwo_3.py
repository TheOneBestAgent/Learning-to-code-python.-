cups_sold = 42
cost_per_cup = 1
price_per_cup = 3

revenue = cups_sold * price_per_cup
cost = cups_sold * cost_per_cup
profit = revenue - cost

print("Revenue: $", revenue)
print("Cost: $", cost)
print("Profit: $", profit)

if profit > 100:
    print("You Killed it today")
else: print("There is always tomorrow")
# Lemonade Stand Profit Calculator
