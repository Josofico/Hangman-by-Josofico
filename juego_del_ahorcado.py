import random
import os
from turtle import right


def random_words():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        [words.append(word.strip("\n")) for word in f]
            
    return words
                        
def user_view(random_word):
    
    count = 5
    hangman = "".join(random_word).upper()
    word_try = "".upper()

    while count > 0:
        os.system("cls")
        print("Can you guess the word?")
        attempts = 0

        for letter in hangman:
            if letter in word_try:
                print(letter, end=" ")
            else:
                print("_", end=" ")
                attempts += 1
        if attempts == 0:
            print("\nGratz, you won.")
            break        

        user_letter = input("\nEnter a letter, pls: ").upper()
        assert user_letter.isalpha(), "Solo puedes ingresar letras"
        word_try += user_letter

        if user_letter not in hangman:
            count -= 1
        if count == 0:
            print(f"Game over.\nThe word is {hangman}")
    
        
   
def run():
    os.system("cls")
    random_word = random.choice(random_words())
    user_view(random_word)
    

if __name__ == '__main__':
    run()