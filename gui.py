import tkinter as tk
from tkinter import messagebox
from connect_four_game import ConnectFour, PLAYER_MAX, PLAYER_MIN, EMPTY
from adversarial_search import alpha_beta
import numpy as np

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four - Human vs AI")
        self.game = ConnectFour()
        self.ai_depth = 4
        self.human_player = PLAYER_MAX
        self.ai_player = PLAYER_MIN

        self.canvas = tk.Canvas(root, width=700, height=600, bg='blue')
        self.canvas.pack()

        self.draw_board()

        self.buttons = []
        for col in range(7):
            btn = tk.Button(root, text=f"Drop in Col {col}", command=lambda c=col: self.make_move(c))
            btn.pack(side=tk.LEFT)
            self.buttons.append(btn)

        self.status_label = tk.Label(root, text="Your turn (Red)", font=('Arial', 14))
        self.status_label.pack()

        reset_btn = tk.Button(root, text="Reset Game", command=self.reset_game)
        reset_btn.pack()

    def draw_board(self):
        self.canvas.delete("all")
        board = self.game.board
        for r in range(6):
            for c in range(7):
                x1 = c * 100
                y1 = r * 100
                x2 = x1 + 100
                y2 = y1 + 100
                color = 'white'
                if board[r][c] == PLAYER_MAX:
                    color = 'red'
                elif board[r][c] == PLAYER_MIN:
                    color = 'yellow'
                self.canvas.create_oval(x1+10, y1+10, x2-10, y2-10, fill=color, outline='black')

    def make_move(self, col):
        if self.game.current_player != self.human_player:
            return

        new_board, row = self.game.transition_state(self.game.board, col, self.human_player)
        if new_board is None:
            messagebox.showerror("Invalid Move", "Column is full!")
            return

        self.game.board = new_board
        self.game.current_player = self.ai_player
        self.game.move_count += 1
        self.draw_board()

        if self.game.is_terminal_state(self.game.board):
            self.end_game()
            return

        self.status_label.config(text="AI thinking... (Yellow)")
        self.root.update()
        ai_move, _ = alpha_beta(self.game.board, self.ai_depth, -float('inf'), float('inf'), True, self.game)
        new_board, row = self.game.transition_state(self.game.board, ai_move, self.ai_player)
        self.game.board = new_board
        self.game.current_player = self.human_player
        self.game.move_count += 1
        self.draw_board()

        if self.game.is_terminal_state(self.game.board):
            self.end_game()
        else:
            self.status_label.config(text="Your turn (Red)")

    def end_game(self):
        if self.game.check_win(self.game.board, self.human_player):
            messagebox.showinfo("Game Over", "You win!")
        elif self.game.check_win(self.game.board, self.ai_player):
            messagebox.showinfo("Game Over", "AI wins!")
        else:
            messagebox.showinfo("Game Over", "It's a draw!")
        self.status_label.config(text="Game Over")

    def reset_game(self):
        self.game = ConnectFour()
        self.draw_board()
        self.status_label.config(text="Your turn (Red)")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ConnectFourGUI(root)
    root.mainloop()