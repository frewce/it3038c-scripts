#count vowels and consonants

print("Give me a lowercase word.")
word = input()
length = (len(word))

vowelCount = 0
consonantCount = 0

for i in word:
    character = i

#brute force way to recognize all vowels
    if (character == 'a' or character == 'e' or character =='i' or character == 'o' or character == 'u' or character == 'A' or character == 'E' or character =='I' or character == 'O' or character == 'U'):
        vowelCount = int(vowelCount) + 1
    else:
        consonantCount = int(consonantCount) + 1

#print all results nicely
print("Total letters: " + str(length))
print("Total vowels: " + str(vowelCount))
print("Total consonants: " + str(consonantCount))