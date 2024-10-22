import random

# Initialize Variables
symbols = ['.', ',', '"', ';', ':', '?', '!', '/', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}']
output = []
text = ""
amount_of_words = 0
pre_data = ""
possible = []
words = []
pairs_of_words = []

# Read Data File
try:
    file = open("data.txt", 'r')
    pre_data = file.read()
    file.close()
except:
    print("Failed")

# Filter out symbols
for i in symbols:
    pre_data = pre_data.replace(i, '')
pre_data = pre_data.lower()

# Create word pairs
words = pre_data.split(' ')
pairs_of_words = []
for i in range(len(words) - 1):
    pairs_of_words.append([words[i], words[i + 1]])

# Randomly pick next word
def next_word(last_word):
    possible = []
    for pairs in pairs_of_words:
        if pairs[0] == last_word:
            possible.append(pairs)
    if len(possible) != 0:
        return possible[random.randrange(0, len(possible))][1]
    else:
        return "the"

# Get user input and create output
try:
    amount_of_words = int(input("Amount of words: "))
    output = input("Text to complete: ").split(' ')
    for i in range(amount_of_words - len(output)):
        print(output[len(output) - 1])
        output.append(next_word(output[len(output) - 1]))
    file = open("output.txt", 'w')
    for i in range(amount_of_words):
        text = text + output[i] + ' '
    file.write(text)
except:
    print("Failed")