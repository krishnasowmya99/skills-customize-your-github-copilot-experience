
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game using Python flow control, string handling, and user input. Learn how to manage game state, validate guesses, and provide feedback while the player tries to guess a hidden word.

## 📝 Tasks

### 🛠️ Create the Hangman game logic

#### Description

Write the main game loop to randomly choose a word from a list, accept letter guesses, and reveal the current progress for the player.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Show the word progress as blanks and revealed letters (e.g. `_ a _ _ m a n`)
- Allow the player to guess one letter at a time
- Track and display correct and incorrect guesses
- Prevent duplicate guess handling

### 🛠️ Add win/lose conditions and messages

#### Description

Implement game completion logic so the player wins when they guess the whole word or loses when they use all attempts.

#### Requirements
Completed program should:

- Limit the number of incorrect guesses
- End the game when the word is guessed or attempts run out
- Display a clear win message when the player succeeds
- Display a clear lose message with the correct word when the player fails
