# Connect Four — Minimax vs Alpha-Beta

This repository contains a Connect Four implementation and experiments comparing Minimax vs Alpha-Beta pruning, plus a simple GUI for Human vs AI play.

## Requirements

- Python 3.8+ (tested)
- numpy
- pandas (for the comparison output table in `main_comparison.py`)
- tkinter (standard with many Python installs; used by the GUI)

Install dependencies with:

```bash
pip install numpy pandas
```

## Files

- `connect_four_game.py`: Game engine and heuristic evaluation. Implements board state, valid moves, transitions, win checks, and the `score_position` heuristic used by the search algorithms.
- `adversarial_search.py`: Search algorithms: `minimax` and `alpha_beta` (alpha-beta pruning), plus utilities to visualize/print the search tree and global counters reporting nodes expanded.
- `gui.py`: Minimal Tkinter GUI to play Human (Red) vs AI (Yellow). The AI uses alpha-beta from `adversarial_search.py` and the game engine from `connect_four_game.py`. Change `ai_depth` in `ConnectFourGUI.__init__` to adjust difficulty.
- `main_comparison.py`: Script that times and compares Minimax vs Alpha-Beta on example board states and prints a results table (uses `pandas` for tabular output). It includes two demonstration experiments (empty board and a mid-game threatening state).

## Quick Usage

- Run the GUI (play against AI):

```bash
python gui.py
```

- Run the comparison experiments (prints timings, nodes expanded, moves, and scores):

```bash
python main_comparison.py
```

- Visualize a search tree from Python (example):

```py
from connect_four_game import ConnectFour
from adversarial_search import visualize_tree

game = ConnectFour()
visualize_tree(game.board, depth=3, algorithm='minimax', game=game)
```

## Notes

- `ai_depth` in `gui.py` controls how deep the AI searches; higher values increase thinking time.
- `adversarial_search.py` tracks global counters `MINIMAX_NODES_EXPANDED` and `AB_NODES_EXPANDED` for experiment logging.
- The heuristic in `connect_four_game.py` (`score_position`) is used to evaluate non-terminal positions when search depth is reached.
