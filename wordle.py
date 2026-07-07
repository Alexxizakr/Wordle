import random #library for random integers
dictionary=["apple", "brave", "stone", "flame", "track"] #array of words (just test words)
word=dictionary[random.randint(0,4)] #random chooses a word in the array
counter=0 #no of gusses
print("_ "*len(word)) # blanks depending on number of words
guess = input("Give a guess:") #enter guess
def wordcountchecker(guess):
    while len(guess) != len(word): #loops until guess and word length are equal
        print("Not the same number of words")
        guess = input("Give a guess:") #ask for another input
wordcountchecker(guess)
counter=counter+1 #add the number of guesses
temp = ["x", "x", "x", "x"] #display for algorithm of wordle since we cant colorcode
def wordle(guess):
    temp = ["x", "x", "x", "x","x"]
    for i in range(0, 5): # for the actual word
        for j in range(0, 5): #for the guess word
            if word[i] == guess[j]: #if the letter in word and guess are equal
                if i == j: #if it is the same position
                    temp[j] = "g"
                else: #f the position is different
                    temp[j] = "y"
    for i in range(0,5):
        print(temp[i],end=" ") #print the temp array without it entering another line
    print()#new line
wordle(guess)


for h in range(0,5):#repeat the loop 5 more times
    if word!=guess: #if the word hasnt correct been guessed
        print("_ " * len(word))
        guess = input("Give a guess:") #ask for input
        wordcountchecker(guess)
        counter = counter + 1 #add to counter
        wordle(guess)

if word==guess:
    print("You guessed the word in",counter,"tries !")
else:
    print("You failed to guess the word,it was",word)
