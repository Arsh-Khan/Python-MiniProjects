import random

def game():
    count = 1
    ncomp = random.randint(1,100)
    ninp = None
    while ninp != ncomp:
        print(f"\nTry No :{count}\n")
        ninp = int(input("Enter a Number between 1 to 100 \n"))
        
        if ninp>ncomp:
            print("\nLower Number Please")
        elif(ninp<ncomp):
            print("\nHigher Number Please")
        else :
            print(f"Your Guess Is Perfect \nYou gussed it in {count} Guesses!")
            with open('hiscore.txt','r') as f:
                highscore = int(f.readline())

            if highscore<count:
                print("You just Broke the High Score")
                with open('hiscore.txt','w') as f:
                    f.write(str(count)) 
       
        count+=1
            

print("\t\t\t\t\t\t\tPerfect Guess Game")
print("\n\nYou Have to Guess the Number Correctly to Win this Game!")

score = game()


