import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number between 1 to 9: ")
while chances<5:
    guess=int(input("Enter Your Guess: "))
    if guess==number:
        print("YOU WON")
        break
    elif guess<number:
        print("Guess a higher number: ",guess)
    else:
        print("Guess a lower number: ",guess)
    chances+=1
if not chances<5:
    print("YOU LOOSE,The number is",number)