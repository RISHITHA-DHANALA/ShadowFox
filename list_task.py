justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print(len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

justice_league.remove("Flash")
justice_league.insert(justice_league.index("Aquaman") + 1, "Superman")

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

justice_league.sort()

print(justice_league)
print(justice_league[0])
