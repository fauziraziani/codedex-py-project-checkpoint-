Rock Paper Scissors Lizard Spock 🪨📄✂️🦎🖖
A Python implementation of the extended version of Rock Paper Scissors, popularized by The Big Bang Theory.


📖 Table of Contents
About

Rules

Features

How to Run

Dependencies

Contributing

License

🎯 About
This is a Python terminal game that expands the classic Rock Paper Scissors with two additional choices: Lizard and Spock, making the game more complex and reducing the chance of ties.

Inspired by The Big Bang Theory, this version follows the rules created by Sam Kass and Karen Bryla.

📜 Rules
The game follows these winning conditions:

Move	Wins Against	Loses Against
✊ Rock	Scissors, Lizard	Paper, Spock
✋ Paper	Rock, Spock	Scissors, Lizard
✌️ Scissors	Paper, Lizard	Rock, Spock
🦎 Lizard	Paper, Spock	Rock, Scissors
🖖 Spock	Rock, Scissors	Paper, Lizard
Each move beats two others and loses to two others, making the game more balanced.

✨ Features
✅ Terminal-based (no GUI required)
✅ Input validation (ensures only valid moves are accepted)
✅ Emoji support (visual representation of choices)
✅ Detailed win/loss messages (explains why a move won)
✅ Random CPU opponent

🚀 How to Run
Clone the repository:

sh
git clone https://github.com/your-username/rock-paper-scissors-lizard-spock.git
cd rock-paper-scissors-lizard-spock
Run the game (Python 3 required):

sh
python rpsls.py
Follow the prompts:

text
================================
Rock Paper Scissors Lizard Spock
================================

1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
Pick a number: 3

You chose: ✌️
CPU chose: 🖖
CPU wins! Spock smashes Scissors
# codedex-py-project-checkpoint-
Rock Paper Scissors Lizard Spock Game
