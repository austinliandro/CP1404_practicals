numbers = [10, 3, 6, -20, 87, 3, -1]
print(numbers)
print(numbers * 2 for number in numbers)
print([number for number in numbers if number > 50])
print([number * 2 for number in numbers if number > 50])
print([number for number in numbers if number < 0])
print([number/2 for number in numbers])
print([number/2 for number in numbers if number > 10])

words = "Hi THERE mum".split()
print(words)
print([word for word in words])
print([word for word in words if len(word) > 2])
print([len(word) for word in words])  # length for each word
print(max(len(word) for word in words))
print([word[1] for word in words])  # first char of each word
print([word.upper() for word in words])
print([word for word in words if word.islower()])
print([word for word in words if word.isupper()])

chars = "Hi THERE Mum"  # without split, it is a string
print(chars)
print([char for char in chars if char.isupper()])
print([char for char in chars if char.islower()])

cars = [["Audi", 2006], ["Jaguar", 2022], ["BMW", 2019], ["Aston Martin", 2021]]

print([car for car in cars])
print([tuple(car) for car in cars])
print([f"{car[0]}" for car in cars])
print([car[0]] for car in cars if car[1] > 2017)
print([car[1] for car in cars])
print([car[1] * 2 for car in cars])
print([max((car[1])) for car in cars])
print([min((car[1])) for car in cars])
print([f"{car[0]} {car[1]}" for car in cars])
