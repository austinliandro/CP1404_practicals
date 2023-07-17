for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("Number of stars: "))
for i in range(n):
    print("*", end=' ')
print()

n = int(input("Number of line: "))
for i in range(n):
    for h in range(0, i + 1):
        print("*", end=' ')
    print()
