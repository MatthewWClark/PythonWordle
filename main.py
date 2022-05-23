from pydoc import doc
import string
import random


#get phrase function that returns phrase for correct amount of points
def getPhrase(guess):
    if guess == 1:
        phrase = "Genius"
    elif guess == 2:
        phrase = "Magnificent"
    elif guess == 3:
        phrase = "Impressive"
    elif guess == 4:
        phrase = "Splendid"
    elif guess == 5:
        phrase = "Great"
    elif guess == 6:
        phrase = "Phew"
    return phrase




#function that returns a list of 3 random words in order
def pick_game_words(wordList):
        word1 = random.choice(wordList)
        word2 = random.choice(wordList)
        word3 = random.choice(wordList)
        randomWords = [word1, word2, word3]
        return randomWords


#function that validates guesses
def validateGuess(guess, guessNum):
    flag = 1
    #checks if length is 5 and if all letters. returns proper error if not
    while(flag==1):
        length = len(guess)
        letters = guess.isalpha()
        if length != 5:
            print("Invalid guess. Please enter exactly 5 characters.")
            guess = str(input(f'{guessNum}? '))
            continue
        if letters == False:
            print("Invalid guess. Please only enter letters.")
            guess = str(input(f'{guessNum}? '))
            continue
        flag = 2
    return guess


#function to play a round of game
def playRound(answer):
    answerList = list(answer)
    turn = 1
    solved = 0
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    returnList = ["X","X","X","X","X"]
    alphabetCorrect = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    #if not solved, ask next guess
    while solved != 1:
        guess = str(input(f'{turn}? '))
        guess = guess.lower()
        guess = validateGuess(guess, turn)
        guessList = list(guess)
        #for letters in guess list, if in same position in answerList, put !. if not in same position but in the word put ?
        #if in neither put #
        #if letter is in right position, put ! in alphabetCorrect list using string.index, etc
        for x in range(5):
            if(guessList[x] == answerList[x]):
                returnList[x] = "!"
                position = string.ascii_lowercase.index(guessList[x])
                alphabetCorrect[position] = "!"
            elif(guessList[x] in answerList):
                returnList[x] = "?"
                position = string.ascii_lowercase.index(guessList[x])
                if (alphabetCorrect[position] != "!"):
                    alphabetCorrect[position] = "?"
            else:
                returnList[x] = "X"
                position = string.ascii_lowercase.index(guessList[x])
                alphabetCorrect[position] = "X"
        #printing output for guess
        print("   ",*returnList, sep = "", end="")
        print("     ", end = "")
        print(*alphabetCorrect, sep="")
        print("  ",guess, end= "")
        print("     ", end = "")
        print(*alphabet_list, sep="")
        #if guess is same as answer, it is solved and calculate points
        if(guess == answer):
            solved = 1
            print(turn)
            points = 2**(6-turn)
            phrase = getPhrase(turn)
            print(f'{phrase}! You earned {points} points this round.')
            break
        #elif turn is 6, user is out of turns and got 0 points
        elif(turn == 6):
            print("You ran out of tries.")
            print(f"The word was {answer}.")
            points = 0
            break
        #else go to next turn
        else:
            turn +=1
    return points

    



def main():
    #reading words from file
    name = ""
    totalScore = 0
    with open("words.txt") as infile:
        words= []
        words = infile.read().splitlines()
    infile.close()
    #picking 3 words
    randomWords = pick_game_words(words)
    menuSel = "x"
    print("Welcome to PyWord.\n")
    while(menuSel != "3"):
        print("----- Main Menu -----")
        print("1. New Game")
        print("2. See Hall of Fame")
        print("3. Quit\n")
        menuSel = str(input(f'What would you like to do? '))
        if menuSel != "1" and menuSel != "2" and menuSel != "3":
            print("\nInvalid choice. Please try again.\n")
            continue
        if menuSel == "1":
            #if play game, enter name and play 3 rounds with the 3 random words. Print name and total score
            name = str(input(f'Enter your player name: '))
            print("\nRound 1:")
            score1 = playRound(randomWords[0])
            print("\nRound 2:")
            score2 = playRound(randomWords[1])
            print("\nRound 3:")
            score3 = playRound(randomWords[2])
            totalScore = score1 + score2 + score3
            print(f'Way to go {name}!\nYou earned a total of {totalScore} points and made it into the Hall of Fame!')
        if menuSel == "2":
            print("\n--- Hall of Fame ---")
            print(" ## : Score : Player")
            if(name != ""):
                print(f'  1 :    {totalScore} : {name}')
            else: print("")
        if menuSel == "3":
            print("Goodbye.")


           
if __name__ == "__main__":
    main()
