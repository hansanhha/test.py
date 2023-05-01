import random
from github_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for _ in range(word_length):
    display.append('_')

end_of_game = False
lives = 6

print(logo)

while not end_of_game :
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for i,letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess

    print(f"{' '.join(display)}")

    if '_' not in display:
        print('You Win')
        end_of_game = True
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that\'s not in the word. You lose a life.")
        if lives == 0:
            print('You Lose')
            end_of_game = True

    print(stages[lives])
