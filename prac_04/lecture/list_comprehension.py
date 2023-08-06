words = input("Enter a sentence: ")
words = words.split()

for word in words:
    print(word)      # it will print the word with list

print([word for word in words])    # it will print the word inside the list