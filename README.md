# 🎮 Tic-Tac-Toe Desktop Game  

A desktop-based **Tic-Tac-Toe** application built with **Python (Tkinter)**.  
The game supports both **Single Player (vs Computer)** and **Two Player** modes with a live **scoreboard**.  


## 🚀 Features  

- ✅ **Two Game Modes**:  
  - Play against the **Computer (AI with basic strategy)**.  
  - Play with a **Friend (2 Player mode)**.  

- ✅ **Scoreboard Tracking**:  
  - In **Computer Mode**: Tracks User Wins, Computer Wins, Losses.  
  - In **2 Player Mode**: Tracks User1 Wins, User2 Wins, Losses.  
  - Scores reset **only when switching modes**.  

- ✅ **Toss Feature**:  
  - At the start of a game vs Computer, a **random toss** decides who goes first (50% chance).  

- ✅ **Smart Gameplay**:  
  - The computer uses a simple AI strategy (tries to win, blocks the user, otherwise plays randomly).  

- ✅ **Dynamic Board Reset**:  
  - After each win or draw, the board resets automatically for continuous play.  
  - If the board fills up, the earliest moves gradually disappear to keep the game flowing.  



## 🛠️ Tech Stack  

- **Language**: Python  
- **GUI Library**: Tkinter  
- **Randomization**: Python’s built-in `random`  



## 📂 Project Structure

    tic_tac_toe/
        │── game.py # Main application code
        │── README.md # Project documentation


## ▶️ How to Run  

1. Make sure you have **Python 3.8+** installed.  
2. Clone or download this repository.  
3. Navigate to the project folder and run:  

```bash
python game.py
```

## 📊 Result

![2 players](https://github.com/LakshmiSrikumar/Tic-Tac-Toe-Unlimited/blob/64f4adfdf1b48da81d511984b061ff8d944668c5/Result/2%20players.jpg)
![Comp vs User](https://github.com/LakshmiSrikumar/Tic-Tac-Toe-Unlimited/blob/64f4adfdf1b48da81d511984b061ff8d944668c5/Result/Comp%20vs%20User.jpg)
![Toss Comp](https://github.com/LakshmiSrikumar/Tic-Tac-Toe-Unlimited/blob/64f4adfdf1b48da81d511984b061ff8d944668c5/Result/Toss%20feature%20(Comp).jpg)
![Toss User](https://github.com/LakshmiSrikumar/Tic-Tac-Toe-Unlimited/blob/64f4adfdf1b48da81d511984b061ff8d944668c5/Result/Toss%20feature%20(User).jpg)
    



