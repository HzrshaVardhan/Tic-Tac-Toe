<h1>Description</h1>
<p1>The following program is an fully functioning game of tic tac toe developed using python 3.12. The module specifically used to develop this game interface was pygame, this module is widely used to assist in developing various video games with it's vast range of code that can ease the game making process on python. The project functions with the data structure's concept of lists; with each move made in the game, the list is altered and can assist in defining the final game state. </p1>

<h1>Logic</h1>
We define a list of size 3 x 3 to act as our tic tac toe playing grid. The current list has values of 0 as no value has been assigned to any of the cells, this is where the game state can be defined. Once Player 1 makes a move, the corresponding cell gains the value of 1, for example: If player 1 plays on the top left corner of the grid, our first value of the list is changed from 0 to 1 defining a new game state. For this code, I have defined Player 2 to have a value of -1 to allow for easier calculation, given we define 1 and -1 for our respective players an end state can be easier to define. If the rows,columns or diagonalls of our list add up to 3, Player 1 Wins. Alternatively, If it adds up to -3: Player 2 Wins. If we get neither 3 or -3 the game state is defined as a tie. 

<h1>How to Play</h1>

1. Decide who plays first

2. The first player is given a cross to start the game
 
3. Players take turns placing a cross or circle in any respective square 

4. First Player to get three of a kind is declared the winner

5. If neither player reach three of a kind the game is tied

<h1>User Interface</h1>

![image](https://github.com/user-attachments/assets/e1716ca4-7aa9-456b-b947-52902746adc0)

Game Interface
 


![image](https://github.com/user-attachments/assets/a42c7bd7-57c1-414f-8d9e-c221a6f217b6)

End Game Screen





