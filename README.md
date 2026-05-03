# 🔴🟡 Connect Four — Minimax vs Alpha-Beta Pruning

A Connect Four AI implementation comparing **Minimax** and **Alpha-Beta Pruning** search algorithms, with a playable Tkinter GUI for Human vs AI matches.

---

## 🧠 AI Overview

Two adversarial search algorithms are implemented and benchmarked head-to-head:

| Algorithm | Description |
|---|---|
| **Minimax** | Full game tree search up to a depth limit; evaluates all possible moves without pruning |
| **Alpha-Beta Pruning** | Minimax with pruning — skips branches that cannot affect the final decision, significantly reducing nodes expanded |

Both algorithms share the same heuristic evaluation function (`score_position`) and are compared on the same board states to measure the pruning efficiency gain.

### Heuristic Evaluation
Non-terminal positions are scored by `score_position` in `connect_four_game.py`, which evaluates:
- **Center column control** — rewarded for occupying the center column
- **Horizontal, vertical, and diagonal windows** — scores 2-in-a-row, 3-in-a-row, and penalizes opponent threats

### Terminal State Scores
- AI wins → `+100,000,000,000,000`
- Opponent wins → `-100,000,000,000,000`
- Draw → `0`

---

## 📊 Algorithm Comparison

Run `python main_comparison.py` to benchmark both algorithms on two board states:
- **Empty board** (depth 4) — worst case for pruning
- **Mid-game threatening state** (depth 5) — where pruning has the most impact

> ⚠️ Results placeholder — run `main_comparison.py` and paste output here

| Board State | Algorithm | Depth | Nodes Expanded | Time (s) | Best Move |
|---|---|---|---|---|---|
| Empty board | Minimax | 4 | — | — | — |
| Empty board | Alpha-Beta | 4 | — | — | — |
| Mid-game | Minimax | 5 | — | — | — |
| Mid-game | Alpha-Beta | 5 | — | — | — |

---

## 🖥️ GUI — Human vs AI

The Tkinter GUI lets you play against the AI (Alpha-Beta, depth 4 by default).

```bash
python gui.py
```

- **You play as Red**, AI plays as Yellow
- Click a column to drop your piece
- Adjust `ai_depth` in `ConnectFourGUI.__init__` to change difficulty (higher = harder but slower)

---

## 🗂️ Project Structure

```
Connect-Four-Game/
│
├── connect_four_game.py     # Game engine: board state, valid moves, win checks, heuristic
├── adversarial_search.py    # Minimax & Alpha-Beta implementations + tree visualizer
├── gui.py                   # Tkinter GUI for Human vs AI play
├── main_comparison.py       # Benchmarking script: nodes expanded, timing, move comparison
└── README.md
```

---

## 🚀 Getting Started

```bash
pip install numpy pandas
python gui.py          # Play against the AI
python main_comparison.py  # Run algorithm comparison
```

> `tkinter` is included with most Python installations. No extra install needed.

---

## 🌳 Search Tree Visualization

You can visualize the search tree in the terminal for debugging or exploration:

```python
from connect_four_game import ConnectFour
from adversarial_search import visualize_tree

game = ConnectFour()
visualize_tree(game.board, depth=3, algorithm='minimax', game=game)
visualize_tree(game.board, depth=3, algorithm='alphabeta', game=game)
```

The tree prints each node as `D{depth} MAX` or `D{depth} MIN` with its children indented below.

---

## 🛠️ Tech Stack

`Python` · `NumPy` · `Pandas` · `Tkinter`

---

## 🏷️ Topics

`minimax` `alpha-beta-pruning` `adversarial-search` `connect-four` `game-ai` `python` `tkinter` `artificial-intelligence` `game-theory`
