# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
# unique_in_order()       == []

def unique_in_order(iterable):
    new_list = []
    if len(iterable) > 0:
        new_list.append(iterable[0])

        for i in range(0, len(iterable)-1):
            if (iterable[i+1] != new_list[len(new_list) - 1]):
                new_list.append(iterable[i+1])

        print(new_list)

unique_in_order([1,2,2,3,3])