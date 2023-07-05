import pyttsx3
import random
from word_list import word_list

#ran_word = random.sample(word_list, 20)
used_words = []
score = 0
got_it_correct = False

random.shuffle(word_list)
ran_word = random.choice(word_list)

name = input("Enter your name: ")
def speak():
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 1.0)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(ran_word)
    engine.runAndWait()



speak()
user_input = input("Spell the word: ").lower()


if user_input == ran_word:
    got_it_correct = True

else:
    got_it_correct = False
    print("Your input is wrong")



while got_it_correct == True:
    score += 1
    print(f"You got the word, that's {score} point/s")
    used_words.append(ran_word)
    #print(used_words)

    #print(score)
    if ran_word in used_words:
        word_list.remove(ran_word)
    #random.shuffle(word_list)
    ran_word = random.choice(word_list)
    speak()
    user_input = input("Spell the word: ").lower()
    if user_input != ran_word:
        print("Your input is wrong")
        print(f'You got {score} point/s. The correct word is, {ran_word}, not {user_input}. Your score is {score} out '
              f'of 360')
        got_it_correct = False

    if len(word_list) == 359:
        print(f"You Won {name}!")
        got_it_correct = False
