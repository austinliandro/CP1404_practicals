"""
CP1404 Practical - Austin Liandro
Count word occurrences in a string
"""

word_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

words = list(word_count.keys())
words.sort()

maximum_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{maximum_length}} : {word_count[word]}")
