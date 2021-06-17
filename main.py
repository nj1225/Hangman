import random 
from words import words
import string

def get_valid_word(words):
  word = random.choice(words) # it takes in a list and randomly chose from that list..
  while '_' in word or ' ' in word: # while dash or space in the word keep chooseing the word.
    word = random.choice(words)

  return word.upper() 


def hangman():


  word = get_valid_word(words)
  word_letters = set(word) #letters in the word we are guessing
  alphabet = set(string.ascii_uppercase)
  used_letters = set() #used for keep track the letters that the user has guessed
  lives = 6

  while len(word_letters)>0 and lives>0:
    #letters used
    #''.join(['a','b','cd']) ->'a b cd'
    print('YOU have',lives ,'lives left and you have used these letters: ' , '  '.join(used_letters))
    # now have to tell the user where the curent alphabet we have in the word and also dash the place where word is not Inputted 
    
   
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Current word: ', ' '.join(word_list))
     #getting user input
    user_letter = input('Guess a letter: ').upper()

    if user_letter in alphabet - used_letters:
        # if the letter guess by user is valid character in the alphabet
      used_letters.add(user_letter)
      if user_letter in word_letters:

        # if the letter that the user guessed is in the word then iam going to remove the letter from it
        word_letters.remove(user_letter)
      else:
        lives = lives - 1 # takes a life away if it is wrong 
        print("letter is not in word") 

    elif user_letter in used_letters :

         # which means they have already used the LETTERS

        
      print("YOU HAVE ALREADY USED THE CHARACTER.PLEASE TRY AGAIN")   
    else:
         # tey typed a wrong character which not in alphabet and used_lettes set
      print("INVALID CHARACTER .PLEASE TRY AGAIN")
  
  # gets here when len(word_letters) == 0 or when lives=0
  if lives == 0:
    print('YOU DIED,SORRY.This word' , word )
  print(" YAHOO YOU HAVE GUESSED THE WORD ." , word , '!!' )




hangman()
#x = hangman()
#print(x.user_letter)




