from collections import Counter, defaultdict, deque, namedtuple

# Counter - Frequency map
print(Counter("banana")) # {'a': 3, 'n': 2, 'b': 1}

# defaultdict - Dict that never raises KeyError
d = defaultdict(list)
d['fruits'].append('apple')

# deque - Double-ended queue (fast appends/pops)
dq = deque([1, 2, 3])
dq.appendleft(0)

# namedtuple - Tuple with field names
Point = namedtuple('Point', ['x', 'y'])
pt = Point(10, 20)
print(pt.x)