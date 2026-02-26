from connect_four_game import ConnectFour, PLAYER_MAX
from adversarial_search import minimax, alpha_beta
import adversarial_search as adv
import time
import numpy as np
import pandas as pd

def reset_counters():
    """Resets global counters before a new search."""
    adv.MINIMAX_NODES_EXPANDED = 0
    adv.AB_NODES_EXPANDED = 0

def run_experiment(search_depth, initial_board=None):
    """Runs a single comparison experiment for a given state and depth."""
    print(f"\n--- Running Experiment at Depth D={search_depth} ---")
    game = ConnectFour()
    if initial_board is not None:
        game.board = initial_board
    
    # --- MINIMAX EXECUTION ---
    reset_counters()
    start_time_minimax = time.time()
    minimax_move, minimax_score = minimax(
        game.board, search_depth, True, game
    )
    end_time_minimax = time.time()
    time_minimax = end_time_minimax - start_time_minimax
    nodes_minimax = adv.MINIMAX_NODES_EXPANDED

    # --- ALPHA-BETA EXECUTION ---
    reset_counters()
    start_time_ab = time.time()
    ab_move, ab_score = alpha_beta(
        game.board, search_depth, -float('inf'), float('inf'), True, game
    )
    end_time_ab = time.time()
    time_ab = end_time_ab - start_time_ab
    nodes_ab = adv.AB_NODES_EXPANDED

    # --- RESULTS ---
    print("\n[Current Board State]:")
    print(game.board)
    print("---------------------------------------")
    
    results = {
        'Algorithm': ['Minimax', 'Alpha-Beta'],
        'Time Taken (s)': [time_minimax, time_ab],
        'Nodes Expanded': [nodes_minimax, nodes_ab],
        'Optimal Move': [minimax_move, ab_move],
        'Score': [minimax_score, ab_score]
    }
    
    df = pd.DataFrame(results)
    
    optimality = "OPTIMAL" if minimax_move == ab_move and minimax_score == ab_score else "MISMATCH"
    
    efficiency = 0 if nodes_minimax == 0 else (nodes_minimax - nodes_ab) / nodes_minimax * 100
    print(f"Decision Consistency: {optimality}")
    print(f"Efficiency Improvement: {efficiency:.2f}% reduction in nodes")
    
    return df

# --------------------------------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------------------------------

if __name__ == "__main__":
    
    # 1. Test Case 1: Empty Board (Neutral State)
    # The algorithms will search from scratch.
    print("--- EXPERIMENT 1: EMPTY BOARD (Neutral State) ---")
    results_empty = run_experiment(search_depth=4)
    print(results_empty.to_markdown(index=False))

    # 2. Test Case 2: Mid-Game State (Threatening State)
    # This state ensures the heuristic gets a complex board to evaluate.
    # Player MAX (1) has a clear 3-in-a-row threat.
    mid_game_board = np.array([
        [ 0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0],
        [-1,  1, -1,  0,  0,  0,  0],
        [ 1,  1,  1,  0, -1, -1,  0]
    ])
    
    print("\n\n--- EXPERIMENT 2: MID-GAME BOARD (Threatening State) ---")
    results_mid = run_experiment(search_depth=4, initial_board=mid_game_board)
    print(results_mid.to_markdown(index=False))