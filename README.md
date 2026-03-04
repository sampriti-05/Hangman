# Hangman
# 🎯 Hangman — The Word Guessing Game

A terminal-based word guessing game written in Python. Test your vocabulary across three difficulty levels before you run out of lives!

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A `Words.txt` file in the same directory as the script (one word per line)

### Running the Game

```bash
python hangman.py
```

---

## 🎮 How to Play

1. Launch the script — you'll be greeted with a welcome message.
2. Press **Y** to start a new game (or **N** to exit).
3. Choose a difficulty level:
   - **E** — Easy
   - **M** — Medium
   - **H** — Hard
4. The game reveals the word's length as a series of underscores (e.g. `_ _ _ _ _`).
5. Guess one letter at a time. Correct guesses fill in the blanks; wrong guesses cost you a life.
6. Win by uncovering the full word before your lives run out!
7. After each round, choose to play again or quit.

---

## ⚙️ Difficulty Levels

| Level  | Word Length | Lives |
|--------|-------------|-------|
| Easy   | < 5 letters | 5     |
| Medium | 5–6 letters | 3     |
| Hard   | 7+ letters  | 4     |

Words are randomly selected from `Words.txt` and sorted into difficulty buckets based on their length.

---

## 📁 Project Structure

```
hangman/
├── hangman.py   # Main game script
└── Words.txt    # Word bank (one word per line)
```

---

## 📝 Notes

- Letter guessing is **case-insensitive** — `A` and `a` are treated the same.
- The game uses **recursion** internally to handle repeated guess attempts within a round.
- Words are stripped of whitespace when loaded but the word bank format should be one word per line for best results.

---

## 🛠️ Possible Improvements

- Add a visual hangman drawing that updates with each wrong guess
- Track and display previously guessed letters
- Add a scoring system across multiple rounds
- Improve recursion-heavy guess loops with iterative alternatives to avoid hitting Python's recursion limit on longer games

---

## 📄 License

This project is for educational and personal use.

