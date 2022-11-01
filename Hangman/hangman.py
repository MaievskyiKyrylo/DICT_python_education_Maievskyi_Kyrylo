import random

print("HANGMAN\nThe game will be available soon")
WORDS = ["python", "java", "javascript", "php", "sausage"]
word = random.choice(WORDS)
wrong = 0
max_wrong = 8
used = []
so_far = "-" * len(word)
print(so_far)
while wrong < max_wrong and so_far != word:
    print("Your attempts :", wrong)
    letter = input("\n\nInput a letter: ")
    if letter != letter.lower():
        print("Please,enter a lowercase English letter")
        continue
    if len(letter) != 1:
        print("You should input a single letter")
        continue
    while letter in used:
        print("You've already guessed this letter")
        letter = input("\n\nInput a letter: ")
    used.append(letter)

    if letter in word:
        new = ""
        for i in range(len(word)):
            if letter == word[i]:
                new += letter
            else:
                new += so_far[i]
        so_far = new
        print(so_far)
    else:
        print("\nThis letter doesn't appear in the word")
        wrong += 1
if wrong == max_wrong:
    print("You dead!")
else:
    print("You survived!")

