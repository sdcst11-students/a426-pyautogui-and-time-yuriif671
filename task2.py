#!working with time

import random
import keyboard
import time

"""
Task 1
Basic Assignment:
Create a program to display 10 characters on screen, one at a time,
to the user.  They have to press that key to advance to the next character.
Tell the user how long it took them to press all 10 characters.

Alternately, you can select a random word from a list of words that you provide.
Have the user type in the word before the next word is selected.  This version
is easier because you can use the existing input() command that you are more
familiar with.

Your assignment should make appropriate use of functions to break the
code up into more manageable sections.  

Your assignment will be graded on the following criteria:

functionality (does it work the way it is intended)
modularity (is it broken up into functions to make your main block momre readable)
appropriate use of return values and input parameters

"""

# The code shown below is one way to read a single 
# keystroke from the keyboard and store it into 
# a variable. We will use it as the basis for this 
# assignment.

#the english alphabet and list of words
words = ['transcription', 'service', 'business', 'which', 'converts', 'speech', 'into', 'written', 'electronic', 'text', 'metallica']

def enterWord():
    print("You have to write the correct words 5 times.")
    start = time.time()
    
    n = 0
    while n < 5:
        word = random.choice(words)
        words.remove(word)

        print("Enter — " + word)
        inputWord = str(input("Enter the word: "))
        if inputWord == word:
            print("Correct!")
            n += 1
        else:
            print("Incorrect!")

    print(f"Good job it took you: {round(time.time() - start, 2)} seconds.")

def main():
    enterWord()
    
if __name__ == '__main__':
    main()