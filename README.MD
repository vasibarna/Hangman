# HANGMAN
Implementation using OOP concepts and reading from file

## Requisitions
Python 3.8.0

### Hangman Game 

The Hangman is a game where a random word is generated and the user must guees the word in maximum 7 attempts.
The first and last letter are automatically shown in the word (and all the appearance of them in the word) 
and are not counted if the user try them again.

### Random Word
The game store a file containing hundreds of words with more than 6 chars. Calling the magic_word function the file is read 
and a random word is prepared to be gueesed by the user.

### Hangman Class
A new class is created and on the class are saved more infos as word, hidden word, number of attempts and gueesed letters.
On the class it is read the word guessed from the user and it is validated, if the input is from ASCII and is 1 char length.

### Main Function
In this module a game object is created with the random word generated. The number of attempts is set to 7. After that the word
is shown on the screen with the first and last letters + their appearances.
In the next part is created the game instance and by using it we are calling all the function already created.

