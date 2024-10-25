# Programmers: Laure Patera
# Course: CS151, Dr.Yalew
# Due Date: 10/24/24
# Programming Assignment: PA 02
# Problem Statement: Create a game of "pick-up sticks" for 2 players and a computer
# Data In: decision to play, number of sticks on the table, number of sticks that players 1 and 3 choose to take, and decision to play again
# Data Out: player losses
# Credits: the readme.file

#Initialize variables and import modules
import random
player_1_loss = 0
player_2_loss = 0
player_3_loss = 0

#Output purpose and ask for number of sticks on the table
print('This program is a game of pick-up sticks played between two users and a computer. Each player picks up a certain number of sticks from a pile on the table, and whoever picks up the last stick loses.')
stick_number = int(input('How many sticks do you want on the table? You can choose any number as an integer between 10 and 100.'))
while 100 < stick_number  or stick_number < 10:
    stick_number = int(input('How many sticks do you want on the table? You can choose any number as an integer between 10 and 100.'))

while stick_number > 0:
    #Player 1 decides how many sticks to take
    player_1_sticks = int(input('Player 1, how many sticks would you like to take, from 1-3?'))
    while 1 > player_1_sticks > 3:
        player_1_sticks = input('Player 1, how many sticks would you like to take, from 1-3?')
    stick_number = stick_number - player_1_sticks
    if stick_number <= 0:
        print('Player 1 lost and the game is over')
        break

    #Computer decides how many sticks to take
    player_2_sticks = random.randint(1, 3)
    stick_number -= player_2_sticks
    print('The computer took', player_2_sticks, 'sticks.')
    if stick_number <= 0:
        print('The computer lost and the game is over')
        player_2_loss += 1
        break

    #Player 3 decides how many sticks to take
    player_3_sticks = int(input('Player 3, how many sticks would you like to take, from 1-3?'))
    while 1 > player_3_sticks > 3:
        player_3_sticks = input('Player 3, how many sticks would you like to take, from 1-3?')
    stick_number = stick_number - player_3_sticks
    if stick_number <= 0:
        print('Player 3 lost and the game is over')
        player_3_loss += 1
        break

#Asks if user would like to play again
play_again = input('Would you like to play again? Enter yes to continue, or no to quit')
play_again.lower()
while play_again != 'yes' and play_again != 'no':
    play_again = input('Would you like to play again? Enter yes to continue, or no to quit')
    play_again.lower()

#For if the user decides to play again
while play_again == 'yes':

    #Asks how many sticks the users want on the table
    stick_number = int(input('How many sticks do you want on the table? You can choose any number as an integer between 10 and 100.'))
    while 100 < stick_number < 10:
        stick_number = int(input('How many sticks do you want on the table? You can choose any number as an integer between 10 and 100.'))

#asks how many sticks player 1 would like to take
    while stick_number > 0:
        player_1_sticks = int(input('Player 1, how many sticks would you like to take, from 1-3?'))
        while 1 > player_1_sticks > 3:
            player_1_sticks = input('Player 1, how many sticks would you like to take, from 1-3?')
        stick_number = stick_number - player_1_sticks
        if stick_number <= 0:
            print('Player 1 lost and the game is over')
            player_1_loss += 1
            break

#finds how many sticks the computer will take
        player_2_sticks = random.randint(1, 3)
        stick_number -= player_2_sticks
        print('The computer took', player_2_sticks, 'sticks.')
        if stick_number <= 0:
            print('The computer lost and the game is over')
            player_2_loss += 1
            break

#Asks how many sticks player 3 would like to take
        player_3_sticks = int(input('Player 3, how many sticks would you like to take, from 1-3?'))
        while 1 > player_3_sticks > 3:
            player_3_sticks = input('Player 3, how many sticks would you like to take, from 1-3?')
        stick_number = stick_number - player_3_sticks
        if stick_number <= 0:
            print('Player 3 lost and the game is over')
            player_3_loss += 1
            break

#Asks if User would like to play again
    play_again = input('Would you like to play again? Enter yes to continue, or no to quit')
    play_again.lower()
    while play_again != 'yes' and play_again != 'no':
        play_again = input('Would you like to play again? Enter yes to continue, or no to quit')
        play_again.lower()

#Outputs losses and thank you to the user
if play_again == 'no':
    print('Player 1 losses:', player_1_loss, '\nComputer losses:', player_2_loss, '\nPlayer 3 losses:', player_3_loss, '\nThank you for playing this program!')

