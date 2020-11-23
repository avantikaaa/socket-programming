# TO RUN THE FILES
	1. “python3 server.py” in one terminal.
	2. Enter a port number for the program to use.
	3. “python3 client.py” in 3 different terminals.
	4. Enter the host name of the system
	5. Enter the same port number given as input to the server.

# ASSUMPTIONS
	1. No extraneous input should be provided.
	2. No terminal(server and/or client) should be closed while running the program.
	3. Commands like ctrl+z or ctrl+c shouldn’t be used.
	4. A player presses the buzzer if and only if they know the correct answer to the question. Once they press the buzzer, they must answer the question. There is no time limit once the buzzer is pressed.

# GAME RULES
	1. There have to be 3 players for the game to start.
	2. A player can use “yes” or “y” (case doesn’t matter- “yEs” is also accepted)
	3. Once the buzzer is pressed, the player must answer the question.
	4. If the buzzer is not pressed within 10 seconds, the next question is displayed.
	5. For every correct answer, the player is awarded 1 point.
	6. For every wrong answer, a player loses 0.5 points.
	7. If a player answers without pressing the buzzer, he loses 1 point.
	8. There are 50 questions in total. The player to reach 5 points first wins the game. If all the 50 questions are exhausted and no player reaches 5 points, the game ends in a draw.

# DESCRIPTION OF THE CODE
	1. Modules used:
		1. Socket
		2. Time: time.sleep() - Used to add delays in output.
		3. Select: Used for the buzzer- Waits for the input for a certain time.
		4. Sys: For input from the clients.
	2. The data of each connection made with the server, each client, is stored in a list.
	3. “utf-8” (8-bit unicode transformation) is used to encode the string while sending a message.
	4. The client and the server are connected by TCP connection.
	5. At the start of the game, each client receives a set of instructions for the game.
	6. Each client is given a number in the order they join the game.
	7. Questions: The question is 1+ question number (to avoid the repetition of questions.
