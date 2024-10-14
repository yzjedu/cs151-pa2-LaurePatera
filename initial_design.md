# Initial Design Document
* Output purpose of the program and instructions to the user
* Create the variable player_1_loss and set it equal to 0 
* Create the variable player_2_loss and set it equal to 0 
* Create the variable player_3_loss and set it equal to 0 
* Ask user to input how many sticks they would like on the table, between 10 and 100 and convert it to an integer, creating the variable stick_number 
* While user input contains any symbols other than numbers,
  * Output to the user, “I did not understand that. Please try again” 
  * Ask user to input how many sticks they would like on the table, between 10 and 100 and convert it to an integer, creating the variable stick_number 
* While user input is greater than 100 or less than 10, 
  * Ask user to input how many sticks they would like on the table, between 10 and 100 and convert it to an integer, creating the variable stick_number 
* While stick_number is greater than 0, continue this code 
  * Output to the user, “player 1, how many sticks would you like to take, from 1-3?” and store the input value with variable player_1_sticks 
  * While player_1_sticks is less than 1 or greater than 3 
    * Output to the user, “player 1, how many sticks would you like to take, from 1-3?” and store the input value with variable player_1_sticks 
    * Subtract player_1_sticks from stick_number 
  * If player_1_sticks is greater than or equal to stick_number, 
    * output “Player 1 lost and the game is over” 
    * Add 1 to the value of player_1_loss 
  * Player 2 will be the computer. Pick a random digit from 1-3, and store this value with variable player_2_sticks 
  * Subtract player_2_sticks from stick number 
  * If player_2_sticks is greater than or equal to stick_number, 
    * output “Player 2 lost and the game is over” 
    * Add 1 to the value of player_2_loss 
  * Output to the user, “player 3, how many sticks would you like to take, from 1-3?” and store the input value with variable player_3_sticks 
  * While player_3_sticks is less than 1 or greater than 3 
    * Output to the user, “player 3, how many sticks would you like to take, from 1-3?” and store the input value with variable player_3_sticks 
    * Subtract player_3_sticks from stick_number 
  * If player_3_sticks is greater than or equal to stick_number, 
    * output “Player 3 lost and the game is over” 
    * Add 1 to the value of player_3_loss 
* Output to the user, “Would you like to play again? Enter ‘yes’ to continue, or ‘no’ to quit”, storing the input with a new variable continue 
* Convert the variable continue to all lower case 
* While continue does not equal yes, or no, 
  * Output to the user, “Would you like to play again? Enter ‘yes’ to continue, or ‘no’ to quit”, storing the input with a new variable continue 
  * Convert the variable continue to all lower case 
* While continue equals yes, 
  * Output purpose of the program and instructions to the user 
  * Create the variable player_1_loss and set it equal to 0 
  * Create the variable player_2_loss and set it equal to 0 
  * Create the variable player_3_loss and set it equal to 0 
  * Ask user to input how many sticks they would like on the table, between 10 and 100 and convert it to an integer, creating the variable stick_number 
  * While user input contains any symbols other than numbers, 
    * Output to the user, “I did not understand that. Please try again” 
    * Ask user to input how many sticks they would like on the table, between 10 and 100 and convert it to an integer, creating the variable stick_number 
  * While user input is greater than 100 or less than 10, 
    * Ask user to input how many sticks they would like on the table, between 10 and 100 and convert it to an integer, creating the variable stick_number 
  * While stick_number is greater than 0, continue this code 
    * Output to the user, “player 1, how many sticks would you like to take, from 1-3?” and store the input value with variable player_1_sticks 
    * While player_1_sticks is less than 1 or greater than 3 
      * Output to the user, “player 1, how many sticks would you like to take, from 1-3?” and store the input value with variable player_1_sticks 
      * Subtract player_1_sticks from stick_number 
    * If player_1_sticks is greater than or equal to stick_number, 
      * output “Player 1 lost and the game is over” 
      * Add 1 to the value of player_1_loss 
    * Player 2 will be the computer. Pick a random digit from 1-3, and store this value with variable player_2_sticks 
    * Subtract player_2_sticks from stick number 
    * If player_2_sticks is greater than or equal to stick_number, 
      * output “Player 2 lost and the game is over” 
      * Add 1 to the value of player_2_loss 
    * Output to the user, “player 3, how many sticks would you like to take, from 1-3?” and store the input value with variable player_3_sticks 
    * While player_3_sticks is less than 1 or greater than 3 
      * Output to the user, “player 3, how many sticks would you like to take, from 1-3?” and store the input value with variable player_3_sticks 
      * Subtract player_3_sticks from stick_number 
    * If player_3_sticks is greater than or equal to stick_number, 
      * output “Player 3 lost and the game is over” 
      * Add 1 to the value of player_3_loss 
  * Output to the user, “Would you like to play again? Enter ‘yes’ to continue, or ‘no’ to quit”, storing the input with a new variable continue 
  * Convert the variable continue to all lower case 
  * While continue does not equal yes, or no, 
    * Output to the user, “Would you like to play again? Enter ‘yes’ to continue, or ‘no’ to quit”, storing the input with a new variable continue 
    * Convert the variable continue to all lower case 
* If continue equals no, 
  * Output to the user, “Player one lost (player_1_loss) times. Player two lost (player_2_loss) times. Player three lost (player_3_loss) times.”
