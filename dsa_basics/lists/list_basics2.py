# MODIFYING ITEMS IN A LIST
sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

sea_creatures[1] = 'octopus'
print(sea_creatures)

sea_creatures[-2] = 'blobfish'
print(sea_creatures)


# SLICING A LIST
print('Slicing using positive indexes.')
print(sea_creatures[1:4])  # The first index is inclusive and the second one is exclusive

print(sea_creatures[:3])
print(sea_creatures[2:])

print('Now slicing using negative indexes.')
print(sea_creatures[-4:-2])
print(sea_creatures[:-3])
print(sea_creatures[-3:])

print('Using stride...')
print(sea_creatures[::2])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[2:9:2])
