import itertools

# Cycle iterator cycles over collection of items indefinitely
seq1 = ["Joe", "John", "Mike"]
cycle1 = itertools.cycle(seq1)
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))

# Count iterator creates simple counter
count1 = itertools.count(100, -10)
print(next(count1))
print(next(count1))
print(next(count1))

