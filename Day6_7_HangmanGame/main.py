import random

from Hangman_words import word_list

chosen_word = random.choice(
    word_list)  #Randomly choose a word from the word_list
word_length = len(chosen_word)
end_of_game = False
lives = 6  #Create a variable called 'lives' to keep track of the number of lives left.

from Hangman_ascii import logo
print(logo)

#Testing code
#print(f"Pssst, the solution is {chosen_word}.")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()  #Ask the user to guess a letter
    if guess in display:  #if user already guessed the letter
        print(f"You have already guessed {guess}")

# If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") #Check guessed letter
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:  #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        #If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
        #If lives goes down to 0 then the game should stop, and it should print "You lose."
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word.upper()}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from Hangman_ascii import stages
    print(
        stages[lives]
    )  #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
