from operator import itemgetter

data = [["Austin", 25], ["Tyler", 29], ["James", 18], ["David", 16]]

print(data[0][1])  # it will print the list inside the list

data.sort()
print(data)    # it will sort the letter A-Z

data.sort(key=itemgetter(1))   # it will sort the number
print(data)