# Flashcard

Flashcard is a simple program that allows the user to review flashcards they have created. 

## How to use Flashcard
### Create a Flashcard file

A flashcard file is a plain text file with some simple syntax. Each line is a new flashcard entry and looks like this:

> Front of card $$$ Back of card:::0

The front and back of card are serperated by 3 dollar signs ($$$). The last number, preceded by three colons (:::) determines if the flashcard entry has been correctly guessed. 0 for no, 1 for yes. It is not required to put these last 4 characters in the flashcard file when creating it. The program will add them automatically. The example.fc file shows an example flashcard file. 

### Run Flashcard

To run Flashcard, in a terminal, call the program followed by the name of the flashcard file:

> $ Flashcard.py example.fc

### Use Flashcard

Flashcard will pick an entry from your flashcard file at random, and show you the front of the card. Try to guess the back of the card. Hit enter to see the back of the card. Then hit Y and enter if you guessed correct, N and enter if you guessed wrong. Flashcard will continue showing you cards that have not been guessed correctly until you have guessed them all. 

At any point you can type a command. Type the 'help' command to see all available commands. 



