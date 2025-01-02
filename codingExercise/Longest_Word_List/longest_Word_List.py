words = ["apple", "banana", "cherry", "blueberry"]

max = len(words[0])
longest = words[0]

for word in words:
    if (len(word) > max):
        max = len(word)
        longest = word

print(f"{longest} is the longest word with {max} characters")