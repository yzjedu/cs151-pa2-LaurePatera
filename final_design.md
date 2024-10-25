### Algorithm:
1. Import random module
2. Initialize variables and set equal to 0
   >1. player_1_loss
   >2. player_2_loss 
   >3. player_3_loss
3. Output to the user, "This program is a game of pick-up sticks played between two users and a computer. Each player picks up a certain number of sticks from a pile on the table, and whoever picks up the last stick loses."
4. Create the variable stick_number and set it equal to the user input given after asking, "How many sticks do you want on the table? You can choose any number as an integer between 10 and 100."

5. while stick_number is less than 10 or greater than 100
   1. Create the variable stick_number and set it equal to the user input given after asking, "How many sticks do you want on the table? You can choose any number as an integer between 10 and 100."
6. While stick_number is greater than 0
   1. Create the variable player_1_sticks and set it equal to the user input given after asking, "Player 1, how many sticks would you like to take, from 1-3?"
   2. While player_1_sticks is less than 1 or greater than 3
      1. Create the variable player_1_sticks and set it equal to the user input given after asking, "Player 1, how many sticks would you like to take, from 1-3?"
   3. set stick_number equal to player_1_sticks subtracted from stick_number
   4. If stick_number is less than or equal to 0
      1. Output to the user, 'Player 1 lost and the game is over'
      2. End the while loop
   5. Set player_2_sticks equal to a random integer between 1 and 3
   6. set stick_number equal to player_2_sticks subtracted from stick_number
   7. If stick_number is less than or equal to 0
      1. Output to the user, 'The computer lost and the game is over'
      2. End the while loop\
   8. Create the variable player_3_sticks and set it equal to the user input given after asking, "Player 3, how many sticks would you like to take, from 1-3?"
   9. While player_3_sticks is less than 1 or greater than 3
      1. Create the variable player_3_sticks and set it equal to the user input given after asking, "Player 3, how many sticks would you like to take, from 1-3?"
   10. set stick_number equal to player_3_sticks subtracted from stick_number
   11. If stick_number is less than or equal to 0
       1. Output to the user, 'Player 3 lost and the game is over'
       2. End the while loop
7. Create the variable play_again and set it equal to the user input after asking the user, "Would you like to play again? Enter yes to continue, or no to quit"
8. convert play_again to lower case
9. While play_again does not equal yes or no
   1. Create the variable play_again and set it equal to the user input after asking the user, "Would you like to play again? Enter yes to continue, or no to quit"
   2. convert play_again to lower case
10. While play_again equals yes
    1. Create the variable stick_number and set it equal to the user input given after asking, "How many sticks do you want on the table? You can choose any number as an integer between 10 and 100."
    2. while stick_number is less than 10 or greater than 100
       1. Create the variable stick_number and set it equal to the user input given after asking, "How many sticks do you want on the table? You can choose any number as an integer between 10 and 100."
    3. While stick_number is greater than 0
       1. Create the variable player_1_sticks and set it equal to the user input given after asking, "Player 1, how many sticks would you like to take, from 1-3?"
       2. While player_1_sticks is less than 1 or greater than 3
          1. Create the variable player_1_sticks and set it equal to the user input given after asking, "Player 1, how many sticks would you like to take, from 1-3?"
       3. set stick_number equal to player_1_sticks subtracted from stick_number
       4. If stick_number is less than or equal to 0
          1. Output to the user, 'Player 1 lost and the game is over'
          2. End the while loop
       5. Set player_2_sticks equal to a random integer between 1 and 3
       6. set stick_number equal to player_2_sticks subtracted from stick_number
       7. If stick_number is less than or equal to 0
          1. Output to the user, 'The computer lost and the game is over'
          2. End the while loop\
       8. Create the variable player_3_sticks and set it equal to the user input given after asking, "Player 3, how many sticks would you like to take, from 1-3?"
       9. While player_3_sticks is less than 1 or greater than 3
          1. Create the variable player_3_sticks and set it equal to the user input given after asking, "Player 3, how many sticks would you like to take, from 1-3?"
       10. set stick_number equal to player_3_sticks subtracted from stick_number
       11. If stick_number is less than or equal to 0
           1. Output to the user, 'Player 3 lost and the game is over'
           2. End the while loop
11. If play_again equals no
    1. Output to the user "Player 1 losses: (player_1_loss) Computer losses: (player_2_loss) Player 3 losses: (player_3_loss) Thank you for playing this program!"
