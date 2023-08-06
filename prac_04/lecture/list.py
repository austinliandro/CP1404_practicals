names = ["Dior", "Gucci"]
print(names)
print(names[0])  # 0 means printing Dior while 1 mean printing Gucci

for name in names:
    print(name)  # to make list going down

text = "Python"

text1 = "Python".split(',')

print(text1)  # it will print the text with []

print(list(text))  # it will make the list of the text inside the []

print(len(names))  # count how many total words

numbers = [3, 5, 7, 8, 23, 56, 93]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers))

numbers.append(89)  # it will add the number
print(numbers)

del numbers[2]   # it will delete the number in the index
print(numbers)

numbers.remove(56)  # it will remove the number that stated inside the numbers.remove
print(numbers)



