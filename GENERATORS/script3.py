def read_numbers():
    for i in range(1, 1000000):
        yield i

total = 0
for n in read_numbers():
    total += n

print(total)
