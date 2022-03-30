# List is a mutable collection of elements

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)
print()

# reading the list elements using positive index
for i in range(0, len(sea_creatures)):
    print(sea_creatures[i])

print()
# Another way to print the list
for i in sea_creatures:
    print(i)
print()

# reading the list elements using negative index
for i in range(1, len(sea_creatures)+1):
    print(sea_creatures[-i])


