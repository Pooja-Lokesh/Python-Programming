# program includes - selection statements : if and elif, while loop; randint 



from random import randint

random_number = randint(1,10)

while True :
    guess = int(input("Enter any number from 1 to 10 :"))
    if guess < random_number :
        print("TOO LOW")
    elif guess > random_number :
        print("TOO HIGH")
    else:
        print("YOU WON")
        choice = input(print("Do you wanna continue with the game ? (y/n)"))
        if choice == "y" :
            random_number = randint(1,10)
            guess = None 
        else :
            print("thank you for playing")
            break
