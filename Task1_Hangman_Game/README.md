# 🎮 Hangman Game

A simple console-based Hangman game developed using Python as part of the **CodeAlpha Python Programming Internship — Month 1**.

---

## 📌 Project Description

This project is a text-based Hangman game where the player attempts to guess a randomly selected word by entering one letter at a time.

The game selects a word from a predefined list of five words. The player can make a maximum of **6 incorrect guesses**. Correctly guessed letters are revealed in the word, while incorrect guesses increase the number of incorrect attempts.

The project is designed to practice basic Python programming concepts such as loops, conditional statements, lists, strings, user input, and random selection.

---

## ✨ Features

- 🎲 Randomly selects a word from a list of 5 predefined words
- 🔤 Allows the player to guess one letter at a time
- ❌ Allows a maximum of 6 incorrect guesses
- ✅ Reveals correctly guessed letters
- 📝 Keeps track of previously guessed letters
- 🚫 Prevents invalid or repeated guesses
- 🖥️ Runs completely in the terminal/console
- 🏆 Displays a winning message when the word is guessed
- 💀 Displays a Game Over message when all attempts are used

---

## 🛠️ Technologies Used

- **Python 3**
- Python `random` module

---

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:

- Variables
- Lists
- Strings
- `random.choice()`
- `while` loops
- `for` loops
- `if-else` statements
- User input using `input()`
- Input validation
- String operations
- Basic program control flow

---

## 🎯 Game Rules

1. The program randomly selects one word from five predefined words.
2. The selected word is initially hidden using underscores.
3. The player enters one letter at a time.
4. If the letter exists in the word, it is revealed.
5. If the letter is incorrect, the incorrect guess counter increases.
6. The player is allowed a maximum of **6 incorrect guesses**.
7. The player wins if all letters of the word are correctly guessed.
8. The game ends when the player guesses the word or reaches the maximum number of incorrect guesses.

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python installation by running:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

### 2. Open the project folder

Open the `Task1_Hangman_Game` folder in VS Code or a terminal.

### 3. Run the program

Use:

```bash
python hangman.py
```

If `python` does not work on Windows, use:

```bash
py hangman.py
```

---

## 📂 Project Structure

```text
Task1_Hangman_Game
│
├── README.md
├── hangman.py
└── hangman_output.png 
```

### File Description

| File | Description |
|---|---|
| `hangman.py` | Main Python program containing the Hangman game |
| `hangman_output.png` | Screenshot showing the gameplay/output |
| `README.md` | Project documentation |

---

## 🖥️ Sample Gameplay

The game starts by displaying the hidden word:

```text
================================
       HANGMAN GAME
================================

Word: _ _ _ _ _ _
Incorrect guesses: 0
Guessed letters: []

Guess a letter:
```

When a correct letter is entered, the letter is revealed:

```text
Word: p _ _ _ _ _
Incorrect guesses: 0
Guessed letters: ['p']

Correct guess!
```

If an incorrect letter is entered:

```text
Wrong guess!
Incorrect guesses: 1
```

The game continues until the player successfully guesses the word or reaches 6 incorrect guesses.

---

## 📸 Gameplay Screenshot

The following screenshot shows the gameplay and program output:

![Hangman Gameplay](hangman_output.png)

---

## 📚 Learning Outcome

Through this project, I practiced building a complete Python program using basic programming concepts.

The project helped me understand:

- How to use lists and strings
- How to generate random selections
- How to create loops for continuous interaction
- How to validate user input
- How to track program state
- How to use conditional statements
- How to build an interactive console application

---

## 💼 Internship Information

This project was completed as part of the **CodeAlpha Python Programming Internship — Month 1**.

### Task

**Task 1: Hangman Game**

### Objective

Create a simple text-based Hangman game where the player guesses a word one letter at a time.

### Requirements Implemented

- 5 predefined words
- Random word selection
- Maximum 6 incorrect guesses
- Basic console input/output
- Python fundamentals

---

## 👨‍💻 Author

**Istikhar Naz**

**CodeAlpha Python Programming Internship — Task 1**

---

## 📄 License

This project was created for educational and internship purposes.
