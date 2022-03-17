# Greedy Algorithm 	 	 

# A thief walks into a house. To his surprise, the thief discovers that the owner of the house has pulverized all his precious metals into fine dust. The thief can thus scoop whatever amount he wants. Because of the density of the precious metals and the amazing strength of his back pack, it can accommodate a total of 580kg dust.

# In the house there is:
# 1. 100kg of gold dust worth $39.95 per gram
# 2. 100kg of platinum dust worth $32.1 per gram
# 3. 200kg of rhodium dust worth $21.54 per gram
# 4. 300kg of palladium dust worth $17.75 per gram
# 5. 500kg of silver dust worth $0.50 per gram

def get_fractions_of_item(item_weights, bag_weight):
    fractions = []
    weight = 0

    for item_wt in item_weights:
        if (weight + item_wt) <= bag_weight:
            weight += item_wt
            fractions.append(1.0)
        else:
            fractions.append(float(bag_weight - weight) / item_wt)
            weight = bag_weight
    return fractions + ([0] * (len(item_weights) - len(fractions)))

items = ['Gold', 'Platinum', 'Rhodium', 'Palladium', 'Silver']
item_weights_in_kg = [100, 100, 200, 300, 500]
item_weights_in_gm = [100000, 100000, 200000, 300000, 500000]
item_prices_per_gm = [39.95, 32.1, 21.54, 17.75, 0.50]
bag_weight = 580

fraction_of_items = get_fractions_of_item(item_weights_in_kg, bag_weight)
print(fraction_of_items)

total_amt = 0
for i in range(0,len(fraction_of_items)):
    total_amt += (fraction_of_items[i] * item_weights_in_gm[i] * item_prices_per_gm[i])

print(total_amt)