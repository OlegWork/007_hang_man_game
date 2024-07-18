import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Gues a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word_list = list(chosen_word)
for i in range(0, len(chosen_word_list)):
    if guess == chosen_word_list[i]:
        print("Right")
    else:
        print("Wrong")
# hm was the using conversion random list element into list itself necessary???
    i +=1

