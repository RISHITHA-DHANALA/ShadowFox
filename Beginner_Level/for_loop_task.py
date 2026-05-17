import random

count_6 = 0
count_1 = 0
double_6 = 0
prev = None

for i in range(20):
    roll = random.randint(1, 6)
    print(roll)

    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1

    if roll == 6 and prev == 6:
        double_6 += 1

    prev = roll

print(count_6)
print(count_1)
print(double_6)

total = 0

for i in range(10):
    total += 10
    print("Are you tired?")
    ans = input()

    if ans.lower() in ["yes", "y"]:
        print(total)
        break

    print(100 - total)

if total == 100:
    print("Congratulations! You completed the workout")
