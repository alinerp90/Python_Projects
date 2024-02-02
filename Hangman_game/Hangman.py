import random

# list of words in the game
from hangman_words import word_list, stages

word = random.choice(word_list)
guess = ""

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

# variable with the _ _ for the word
display = []
word_length = len(word)

for _ in word:
    display += "_"

lives = 6

end_game = False
letters_guessed = ""

while not end_game:
    print(stages[lives])
    guess = input("Guess the letter:").lower()
    
    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    if guess not in word:
        lives -= 1
        letters_guessed += guess
        print(f"You have {lives} lives")
        print(f"Letters already guessed: {letters_guessed}")
    print(" ".join(display))

    if "_" not in display:
        end_game = True
        print("You win.")
    
    if lives == 0:
        end_game = True
        print(stages[0])
        print("You lose")
        print(f"The word was: {word}")


# for position in range(word_length):
#     letter = word[position]
#     if letter == guess:
#         display[position] = letter
# print(display)


