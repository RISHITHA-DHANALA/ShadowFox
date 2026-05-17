def format_value(a, b):
    return format(a, b)

result = format_value(145, 'o')
print(result)

radius = 84
pi = 3.14

area = pi * radius * radius
print(int(area))

water_per_sq_m = 1.4
total_water = area * water_per_sq_m
print(int(total_water))

distance = 490
time = 7 * 60

speed = distance / time
print(int(speed))
