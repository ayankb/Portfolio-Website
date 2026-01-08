import sqlite3


projects = [
    {
        "title": "Coding Battle Ground",
        "description": "It is a real-time, multiplayer coding challenge platform built using Flask, Socket.IO, and the Judge0 API. It allows users to join coding rooms, compete in timed challenges, submit code in multiple programming languages, and view real-time leaderboards.",
        'link': 'https://github.com/ayankb/CodingBattleGround',
        'image': 'CodingBattleGround.png'
    },
    {
        "title": "Hangman Game",
        "description": "Simple Hangman Game using python.",
        'link': 'https://github.com/ayankb/Hangman',
        'image': 'hangman.png'
    },
    {
        "title": "Blackjack Game",
        "description": "Welcome to the classic game of Blackjack — built entirely with Python! This is a simple terminal-based Blackjack (21) game where you play against the computer. It's a fun little project that showcases core Python skills like functions, control flow, and randomization.",
        'link': 'https://github.com/ayankb/blackjack',
        'image': 'blackjack.png'
    },
    {
        "title": "Snake Game 🐍",
        "description": "A classic Snake game built using Python's turtle module. Eat the food, grow longer, and avoid crashing into walls or yourself!",
        'link': 'https://github.com/ayankb/snake-game',
        'image': 'snakegame.png'
    },
    {
        
        "title": "🏓 Pong Game",
        "description": "A classic Pong game implemented using Python.",
        'link': 'https://github.com/ayankb/Pong-Game',
        'image': 'ponggame.png'
    },
    {
        "title": "Morse Code Converter",
        "description": "A simple Python program to Encrypt text into Morse Code and Decrypt Morse code into text.",
        'link': 'https://github.com/ayankb/Morse-Code-Converter',
        'image': 'morse-code-in-python.png'
    },
]

con = sqlite3.connect('instance/project.db')
cursor = con.cursor()

for project in projects:
    cursor.execute('''
        INSERT INTO Project (title, description, link, image)
        VALUES(?, ?, ?, ?)
        ''', (
            project['title'],
            project['description'],
            project['link'],
            project['image']
        )
    )

con.commit()
con.close()
