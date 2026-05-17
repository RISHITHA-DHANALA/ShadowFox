import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Meena", "Kiran", "Divya"],
    "Math": [78, 45, 89, 66, 92],
    "Science": [88, 56, 91, 70, 85],
    "English": [75, 60, 84, 72, 90]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

print(df)

print("\nTop Performer:")
print(df.loc[df["Total"].idxmax()])
