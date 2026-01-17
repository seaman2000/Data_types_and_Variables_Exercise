number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

is_sword_broken = False
is_helmet_broken = False
expenses = 0.00
counter = 0

for lost_fight in range(1 , number_of_lost_fights + 1):

    if lost_fight % 2 == 0:
        expenses += helmet_price
        is_helmet_broken = True
    if lost_fight % 3 == 0:
        expenses += sword_price
        is_sword_broken = True
    if is_helmet_broken and is_sword_broken:
        expenses += shield_price
        counter += 1
        if counter % 2 == 0:
            expenses += armor_price

    is_sword_broken = is_helmet_broken = False

print(f"Gladiator expenses: {expenses:.2f} aureus")
