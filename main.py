#Hangman game

import random

word_list = ["ardvark", "baboon", "camel", "towel", "symphony", "orchestra", "chair"]

chosen_word = random.choice(word_list)

print(f"psst...the word is {chosen_word}")

display = []

for _ in range(len(chosen_word)):
    display += "_"

print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
