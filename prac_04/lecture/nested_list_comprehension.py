things = []
for x in range(1, 4):
    for y in range(1, 4):
        print(f"{x} + {y} = {x + y}")
        things.append(x + y)
print(things)

things.append([x + y for x in range(1, 4) for y in range(1, 4)])
print(things)