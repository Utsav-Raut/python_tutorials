# The point of knowing iterators and iterables is so that we can add these methods to our own classes and make them iterable as well.

# We now build a class that behaves like the built-in "range" function

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    

nums = MyRange(1, 10)

# for num in nums:
#     print(num)

# print(next(nums))
# print(next(nums))
# print(next(nums))


# Generators are iterators as well but the dunder iter() and dunder next() methods are created automatically and hence we need not create those methods as we did above.

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

# print(next(nums))
# print(next(nums))
# print(next(nums))

# OR
for num in nums:
    print(num)


# Iterators need not end and can go on forever as long as there is a next value
