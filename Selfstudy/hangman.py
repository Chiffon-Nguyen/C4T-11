import time
import random

name = input("What is your name? ")
print ("Hello, %s" %name + ". Time to play hangman!")
print ('''
''')
#wait for 1 second
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)

numof_rightans = 0

while True:
    wordList = ['succulent','cultivate','monarch','demolish','obesity','casserole','penguin','unnecessary','preparatory']
    if wordList == []:
        print("You have no words in list")
    print("Do you want to add words?")
    newWord_orNot = str(input("If yes: enter YES. If no: enter NO" + '\n' + ""))
    if newWord_orNot.upper() == "YES":
        newWordString = (str(input("Enter new words to default list, seperated by space: ")))
        newWordList = newWordString.split(" ")
        wordList.extend(newWordList)
    elif wordList == []:
        print("End game")
        break
    wordtoGuess = wordList[random.randint(0,len(wordList))]
    wordList.remove(wordtoGuess)
    guess = ''
    numOfGuess = int(1.5*len(wordtoGuess))

    if numOfGuess == 0:
        print("You lose")
        playAgain = input("Wanna play another game?", '\n', "If not, enter NO. If yes, enter YES", '\n')
        if playAgain.upper().startswith("Y") == True:
            continue
        else:
            print("End game")
            break

    print("By default, you have", numOfGuess, "guesses. Do you wish to change?")
    changeNumOfGuess = str(input("If yes, enter YES. If no, enter NO" + '\n' + ""))
    while True:
        if changeNumOfGuess.upper().startswith("Y") == True:
            upperLimit = int(2*len(wordtoGuess) + 1)
            numOfGuess = int(input("Enter your wished number of guesses fewer than " + str(upperLimit) + ": "))
            if numOfGuess < upperLimit:
                print("You'll have %i" %numOfGuess, "guesses")
                break
            else: 
                print("It is not valid. Please enter another number")
                continue
        else:
            print("You have", int(len(wordtoGuess)), "by default")
    print("This word has ", len(wordtoGuess), "characters") 
    print("_ " *len(wordtoGuess)) 

    while numOfGuess > 0:
        CharOrWord = input("Do you wanna guess a char or the whole word? If a char, enter C. If a word, enter W \n")
        if CharOrWord.upper().startswith("C") == True:
            guessCh = str(input("Enter a character: "))
            if guess.isalpha() and len(guessCh) == 1:
                if guessCh in wordtoGuess:
                    numOf_RightGuess = wordtoGuess.count(guessCh)
                    if numOf_RightGuess == 1:
                        print("There is", numOf_RightGuess, guessCh)
                    else: 
                        print("There are", numOf_RightGuess, str(guessCh) + "'s")
                    print ("You have", numOfGuess, "more guesses")
                else:
                    print("You're wrong")
                    numOfGuess -= 1
                    print ("You have", numOfGuess, "more guesses")
            else: 
                print("Invalid input. Please re-enter.")
        elif CharOrWord.upper().startswith("W") == True:
            guessWo = str(input("Enter a word: "))
            if guess.isalpha() and len(guessCh) == len(wordtoGuess):
                




