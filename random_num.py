import random
import sys

print("RANDOM NUMBER GUESSING GAME!")

r = random.randint(0,100)
n = int(input("Enter a number to begin: ")) 
count1 = 0

while r != n:
    if n > r:
        print("You've guessed too high.")
        n = int(input("Enter a number to begin: ")) 
        count1+=1
    if n < r: 
        print("You've guessed too low.")
        n = int(input("Enter a number to begin: ")) 
        count1+=1
    if n == r:
        print("Congratulations!, you found the no. in " +str(count1)+ " tries")

    if count1 > 10:
        print("All attempts exhausted! Restart the game.")
        sys.exit()    
