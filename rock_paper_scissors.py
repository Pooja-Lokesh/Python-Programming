# Play rock-paper-scissors with your pc 


from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score :
    print(f" Player score : {player_wins} , Computer score : {computer_wins}")
    print("....ROCK....")
    print("....PAPER....")
    print("....SCISSORS...")

    player = input("enter your choice :").lower()
    if player == "quit" :
        break
    random_num = randint(1,3)
    if random_num == 1 :
        computer = "rock"
    elif random_num == 2 :
        computer = "paper"
    else:
        computer = "scissors"

    print(f"the computer plays {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" :
        if computer == "paper" :
            print("computer wins")
            computer_wins += 1
        else :
            print("player wins")
            player_wins += 1
    elif player == "paper" :
        if computer == "rock" :
            print("player wins")
            player_wins += 1
        else :
            print("computer wins")
            computer_wins += 1
    elif player =="scissors" :
        if computer == "paper" :
            print("player wins")
            player_wins += 1
        else :
            print("computer wins")
            computer_wins += 1
    else:
        print("enter a valid value")

if player_wins > computer_wins :
    print("CONGRATS !! YOU WIN")
elif player_wins == computer_wins :
    print("IT'S A TIE")
else :
    print("SORRY.. COMPUTER WINS")
