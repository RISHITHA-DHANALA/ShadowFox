height = float(input())
weight = float(input())

bmi = weight / (height * height)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")

city = input()

if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print(city + " is in Australia")
elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print(city + " is in UAE")
elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print(city + " is in India")

city1 = input()
city2 = input()

if (city1 in ["Mumbai", "Bangalore", "Chennai", "Delhi"] and city2 in ["Mumbai", "Bangalore", "Chennai", "Delhi"]):
    print("Both cities are in India")
elif (city1 in ["Sydney", "Melbourne", "Brisbane", "Perth"] and city2 in ["Sydney", "Melbourne", "Brisbane", "Perth"]):
    print("Both cities are in Australia")
elif (city1 in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] and city2 in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]):
    print("Both cities are in UAE")
else:
    print("They don't belong to the same country")
