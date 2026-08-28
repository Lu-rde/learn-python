# Rock, paper, scisors game

import random 

print ("WELCOME TO ROCK, PAPER, SCISORS !!!" \
" \n Type ROCK, PAPER, SCISORS to play  :)" \
"\n or quit to end game ")

weapon = ["ROCK", "PAPER", "SCISORS"]
rounds_played = 0
user_points = 0

while True :
    user_choice = input ("Choose your weapon : ").upper()
    computer_choice = random.choice (weapon)
    if user_choice == "QUIT" :
            break
    
    if user_choice in weapon:
        print (f" Computer choice : " , computer_choice)

    if user_choice == computer_choice:
        print ("\n TIE")
        rounds_played +=1

    elif user_choice == "ROCK" and computer_choice=="SCISORS" :
        print ("\n YOU WIN !!!")
        rounds_played +=1
        user_points += 1

    elif user_choice == "PAPER" and computer_choice=="ROCK" :
        print ("\n YOU WIN !!!")
        rounds_played += 1
        user_points += 1

    elif user_choice == "SCISORS" and computer_choice=="PAPER" :
        print ("\n YOU WIN !!!")
        rounds_played +=1
        user_points += 1

    else : 
            print ("\n YOU LOSE")
            rounds_played +=1

    print (f"\n ROUNDS PLAYED: {rounds_played}, YOUR POINTS : {user_points}")

print (f"\n ROUNDS PLAYED: {rounds_played}, YOUR POINTS : {user_points}")

print ("\n GAME OVER")