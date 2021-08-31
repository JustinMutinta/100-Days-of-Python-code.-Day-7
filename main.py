#Hangman game

import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear


print(logo)
chosen_word = random.choice(word_list)

lives = 6

print(f"psst...the word is {chosen_word}")

display = []

for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!!!")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(stages[lives])
