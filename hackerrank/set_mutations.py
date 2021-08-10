# We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations 
# do not make any changes or mutations to the set.

# We can use the following operations to create mutations to a set:

# .update() or |=
# Update the set by adding elements from an iterable/another set.

H = set("Hacker")
R = set("Rank")
print(H)

H.update("R")
print(H)

# **************************************

# .intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.

H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print(H)

# **************************************

# .difference_update() or -=
# Update the set by removing elements found in an iterable/another set.

H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print(H)

# **************************************

# .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.

H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)

print(H)
