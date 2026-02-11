import random

print(random.random())           # Float 0.0 to 1.0
print(random.randint(1, 10))     # Integer 1 to 10
items = ['apple', 'banana', 'cherry']
print(random.choice(items))      # Pick one
random.shuffle(items)            # Shuffle in-place
print(random.sample(items, 2))   # Pick 2 unique items