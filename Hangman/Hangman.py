import random
import Hangman_art
import Hangmanwords

print(Hangman_art.logo)

chosen_word = random.choice(Hangmanwords.word_list)

word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"

while '_' in display and lives != 0:
  guess = input("Guess a letter: ").lower()
  if guess in display:
      print("You have already guessed this letter right :). Try another!")
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
      print(f"Your guess {guess}, that's not in the word. You loose a life")
      lives -= 1
      print(Hangman_art.stages[lives])
      if lives == 0:
        print("You lose")  
        print(f"It was {chosen_word}!")

  print(f"{' '.join(display)}")
  if "_" not in display:
        end_of_game = True
        print("You Win.")