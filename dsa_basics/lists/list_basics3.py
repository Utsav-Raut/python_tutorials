# MODIFYING LISTS WITH OPERATORS

oceans = ['Indian', 'Atlantic', 'Pacific', 'Southern', 'Arctic']
sea_creatures = ['shark', 'octopus', 'blob fish', 'mantis shrimp', 'anemone']

print(oceans + sea_creatures)

sea_creatures = sea_creatures + ['yeti crab']
print(sea_creatures)

print('Repeating some values')
print(oceans * 3)

# REMOVING AN ITEM FROM A LIST
print('Now we delete some elements.....')
del sea_creatures[2]
print(sea_creatures)

del sea_creatures[1:4]
print(sea_creatures)


# CONSTRUCTING LIST WITH LIST ITEMS
print('Constructing lists with lists.....DUH!!!')
sea_names = [['shark', 'octopus', 'squid', 'mantis shrimp'],['Sammy', 'Jesse', 'Drew', 'Jamie']]
print(sea_names[1][0])
print(sea_names[1][2])

for i in range(0, len(sea_names)):
    for j in range(0, len(sea_names[i])):
        print(f'[{i}][{j}] = {sea_names[i][j]}')