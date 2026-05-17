friends = ["Ravi", "Anita", "John", "Kiran", "Meena"]

friend_tuples = []

for name in friends:
    friend_tuples.append((name, len(name)))

print(friend_tuples)

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transport": 500,
    "Fun": 300,
    "Misc": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transport": 600,
    "Fun": 400,
    "Misc": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(your_total)
print(partner_total)

if your_total > partner_total:
    print("You spent more")
else:
    print("Partner spent more")

for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    print(key, diff)
