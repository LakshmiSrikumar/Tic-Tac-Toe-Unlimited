import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Widget")

        # Game mode: "Computer" (vs AI) or "2P" (two players)
        self.mode = tk.StringVar(value="Computer")  
        self.turn = "X"                      # Current turn ("X" or "O")
        self.board = [""] * 9                # Internal board representation
        self.move_count = 0                  # Count moves played so far
        self.scores = {                      # Scoreboard for different modes
            "User":0, "Computer":0, "Win":0, "Loss":0,
            "User1":0, "User2":0
        }
        self.last_mode = self.mode.get()     # Track last mode for resetting

        # --- Mode Selection UI ---
        tk.Label(root, text="Choose Mode:").grid(row=0, column=0, columnspan=3)
        tk.Radiobutton(root, text="Vs Computer", variable=self.mode, value="Computer", 
                       command=self.reset_scoreboard).grid(row=1, column=0, columnspan=3)
        tk.Radiobutton(root, text="2 Players", variable=self.mode, value="2P", 
                       command=self.reset_scoreboard).grid(row=2, column=0, columnspan=3)

        # --- Scoreboard Display ---
        self.score_label = tk.Label(root, text="", font=("Arial", 12))
        self.score_label.grid(row=3, column=0, columnspan=3)

        # --- Turn Info Display ---
        self.turn_label = tk.Label(root, text="Turn: X", font=("Arial", 12, "bold"))
        self.turn_label.grid(row=4, column=0, columnspan=3)

        # --- Game Board (3x3 Buttons) ---
        self.buttons = []
        for i in range(9):
            btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                            command=lambda i=i: self.play(i))
            btn.grid(row=5 + i // 3, column=i % 3)
            self.buttons.append(btn)

        # Initialize scoreboard and board
        self.reset_scoreboard()

    # Reset scoreboard text based on mode
    def reset_scoreboard(self):
        # If mode changed, reset scores
        if self.mode.get() != self.last_mode:
            for key in self.scores:
                self.scores[key] = 0
            self.last_mode = self.mode.get()

        # Update scoreboard text
        if self.mode.get() == "Computer":
            self.score_text = (
                f"User: {self.scores['User']}   Computer: {self.scores['Computer']}   "
                f"Win: {self.scores['Win']}   Loss: {self.scores['Loss']}"
            )
        else:
            self.score_text = (
                f"User1: {self.scores['User1']}   User2: {self.scores['User2']}   "
                f"Win: {self.scores['Win']}   Loss: {self.scores['Loss']}"
            )

        self.score_label.config(text=self.score_text)

        # Reset the game board silently
        if hasattr(self, "buttons"):
            self.reset_board()

    # Update scoreboard after a winner is determined
    def update_scoreboard(self, winner):
        if winner == "User":
            self.scores["User"] += 1
            self.scores["Win"] += 1
        elif winner == "Computer":
            self.scores["Computer"] += 1
            self.scores["Loss"] += 1
        elif winner == "User1":
            self.scores["User1"] += 1
            self.scores["Win"] += 1
        elif winner == "User2":
            self.scores["User2"] += 1
            self.scores["Loss"] += 1
        self.reset_scoreboard()

    # Reset the game board for a new round
    def reset_board(self):
        self.board = [""] * 9
        self.move_count = 0
        for btn in self.buttons:
            btn.config(text="", state="normal")

        # --- Toss feature for vs Computer mode ---
        if self.mode.get() == "Computer":
            self.turn = random.choice(["X", "O"])  # Randomly choose who starts
            if self.turn == "X":
                self.turn_label.config(text="Toss Result: User starts (X)")
            else:
                self.turn_label.config(text="Toss Result: Computer starts (O)")
                # Delay ensures UI updates before computer moves
                self.root.after(500, self.computer_play)
        else:
            self.turn = "X"
            self.turn_label.config(text="Turn: X")

    # Handle a player move at position i
    def play(self, i):
        if self.board[i] != "":  # Ignore if cell already filled
            return

        # Place mark on board and button
        self.board[i] = self.turn
        self.buttons[i].config(text=self.turn)

        # Check if this move wins the game
        if self.check_winner(self.turn, self.board):
            if self.mode.get() == "Computer":
                winner_name = "User" if self.turn == "X" else "Computer"
            else:
                winner_name = "User1" if self.turn == "X" else "User2"

            self.update_scoreboard(winner_name)
            self.reset_board()
            return

        # Switch turn
        self.turn = "O" if self.turn == "X" else "X"
        self.turn_label.config(text=f"Turn: {self.turn}")
        self.move_count += 1

        # --- Rolling board mechanic ---
        # When 8 moves played, the earliest move is cleared to keep board dynamic
        if self.move_count >= 8:
            idx = self.move_count - 8
            if 0 <= idx < 9:
                self.board[idx] = ""
                self.buttons[idx].config(text="")

        # If computer's turn, let AI play
        if self.mode.get() == "Computer" and self.turn == "O":
            self.root.after(200, self.computer_play)

    # Computer move using minimax strategy
    def computer_play(self):
        best_score = -10_000
        best_move = None
        for i in range(9):
            if self.board[i] == "":
                # Try move
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                # Track best move
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            self.play(best_move)

    # Minimax algorithm for optimal play
    def minimax(self, board, depth, is_maximizing):
        # Base cases: check for terminal states
        if self.check_winner("O", board):
            return 10 - depth
        if self.check_winner("X", board):
            return depth - 10
        if all(cell != "" for cell in board):
            return 0  # Draw

        if is_maximizing:  # Computer's turn
            best_score = -10_000
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:  # Opponent's turn
            best_score = 10_000
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    # Check if a given mark ("X" or "O") has won
    def check_winner(self, mark, board=None):
        b = board if board is not None else self.board
        win_patterns = [
            (0,1,2),(3,4,5),(6,7,8),  # Rows
            (0,3,6),(1,4,7),(2,5,8),  # Columns
            (0,4,8),(2,4,6)           # Diagonals
        ]
        return any(b[a] == b[b_idx] == b[c] == mark for a,b_idx,c in win_patterns)


# --- Run the Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    app.reset_board()  # Start game with toss
    root.mainloop()
