import random

def shuffleword(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)
def printPuzzleQuestions(word,score):
    problemWord=shuffleword(word)
    print("Arrange the letters to vailed form \n",problemWord)
    userword=input("Enter the correct word ")
    print()
    if userword.upper()==word:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
        score-=1
    return score
def main():
    score=0
    words=["ELEPHANT","APPLE","COURSE","IRRELIVANT","REMOVE","SUFFICIENT","INSTANCE"]
    words=random.sample(word,k=len(word))

    for word in words:
        score=printPuzzleQuestions(word,score)
        print("Your score is ",score)
        print()
    main()


