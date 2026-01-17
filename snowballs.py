snowballs_being_made = int(input())
max_value = float('-inf')
max_weight = 0
max_time_needed = 0
max_quality = 0


for snowball in range(snowballs_being_made):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight // time_needed) ** quality

    if snowball_value > max_value:
        max_value = snowball_value
        max_quality = quality
        max_weight = weight
        max_time_needed = time_needed

print(f"{max_weight} : {max_time_needed} = {max_value} ({max_quality})")