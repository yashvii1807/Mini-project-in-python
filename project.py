import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the taget : "))
    if (userChoice == target):
        print ("Success : correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was to big. Take a smaller guess..")
        
print("----Game Over----")        