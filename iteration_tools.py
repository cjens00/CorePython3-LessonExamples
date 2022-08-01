from itertools import islice, count

# Use itertools.islice() to lazily slice a generator sequence
# itertools.count(firstval=0, step=1)
thousand_squares = islice((x * x for x in count()), 1000)
print(thousand_squares)
print(list(thousand_squares)[-10:])

booleanValues = [False, False, False, True]
anyVal = any(booleanValues)
allVal = all(booleanValues)

print(anyVal)
print(allVal)

# str("Title").title() returns true.
# True if first character is uppercase
# and remaining characters are lowercase.
cities = ["San Francisco", "Seattle", "Tokyo"]
print(all(city.title() for city in cities))

# zip() function - Synchronizes iteration across two or more iterables.
# zip() called with n iterables yields n-tuples when iterated.
r0 = [x for x in range(10)]
r10 = [x for x in range(10, 20)]
r20 = [x for x in range(20, 30)]

for item in zip(r0, r10, r20):
    print(item)
