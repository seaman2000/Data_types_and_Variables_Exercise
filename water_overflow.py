number_of_lines = int(input())

capacity_of_water_tank = 255

for _ in range(number_of_lines):
    new_line = int(input())

    if capacity_of_water_tank < new_line:
        print("Insufficient capacity!")
        continue
    capacity_of_water_tank -= new_line

print(255 - capacity_of_water_tank)

