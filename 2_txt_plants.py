data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


plants_filename = 'flower_write.txt'

# writing file using write function

# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         plants.write(plant)



# Writing file using print function

with open(plants_filename, 'w') as plants:
    for plant in data:
        if plant[0] == 'S':
            x = '- 1'
        else:
            x = '- 0'

        print(plant, x,  file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
# print(new_list)
