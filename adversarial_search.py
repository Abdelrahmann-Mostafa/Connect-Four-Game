import time
from connect_four_game import ConnectFour, PLAYER_MAX, PLAYER_MIN, EMPTY

MINIMAX_NODES_EXPANDED = 0
AB_NODES_EXPANDED = 0

def minimax(board, depth, is_maximizing_player, game, collect_tree=False):
    """
    Minimax implementation for Connect Four (full tree search up to depth limit).
    """
    global MINIMAX_NODES_EXPANDED
    MINIMAX_NODES_EXPANDED += 1

    valid_moves = game.get_valid_moves(board)
    is_terminal = game.is_terminal_state(board)

    tree = {'label': f"D{depth} {'MAX' if is_maximizing_player else 'MIN'}", 'children': []} if collect_tree else None

    if depth == 0 or is_terminal:
        if is_terminal:
            if game.check_win(board, PLAYER_MAX):
                score = 100000000000000
            elif game.check_win(board, PLAYER_MIN):
                score = -100000000000000
            else:
                score = 0
        else:
            score = game.score_position(board, PLAYER_MAX)
        return (None, score, tree) if collect_tree else (None, score)

    if is_maximizing_player:
        value = -float('inf')
        best_move = valid_moves[0]

        for col in valid_moves:
            new_board, row = game.transition_state(board, col, PLAYER_MAX)
            
            result = minimax(new_board, depth - 1, False, game, collect_tree)
            new_score = result[1]
            if collect_tree:
                tree['children'].append(result[2])

            if new_score > value:
                value = new_score
                best_move = col
        
        return (best_move, value, tree) if collect_tree else (best_move, value)

    else:
        value = float('inf')
        best_move = valid_moves[0]

        for col in valid_moves:
            new_board, row = game.transition_state(board, col, PLAYER_MIN)
            
            result = minimax(new_board, depth - 1, True, game, collect_tree)
            new_score = result[1]
            if collect_tree:
                tree['children'].append(result[2])

            if new_score < value:
                value = new_score
                best_move = col

        return (best_move, value, tree) if collect_tree else (best_move, value)


def alpha_beta(board, depth, alpha, beta, is_maximizing_player, game, collect_tree=False):
    """
    Alpha-Beta Pruning implementation for Connect Four.
    """
    global AB_NODES_EXPANDED
    AB_NODES_EXPANDED += 1

    valid_moves = game.get_valid_moves(board)
    is_terminal = game.is_terminal_state(board)

    tree = {'label': f"D{depth} {'MAX' if is_maximizing_player else 'MIN'}", 'children': []} if collect_tree else None

    if depth == 0 or is_terminal:
        if is_terminal:
            if game.check_win(board, PLAYER_MAX):
                score = 100000000000000
            elif game.check_win(board, PLAYER_MIN):
                score = -100000000000000
            else:
                score = 0
        else:
            score = game.score_position(board, PLAYER_MAX)
        return (None, score, tree) if collect_tree else (None, score)

    if is_maximizing_player:
        value = -float('inf')
        best_move = valid_moves[0]

        for col in valid_moves:
            new_board, row = game.transition_state(board, col, PLAYER_MAX)
            result = alpha_beta(new_board, depth - 1, alpha, beta, False, game, collect_tree)
            new_score = result[1]
            if collect_tree:
                tree['children'].append(result[2])

            if new_score > value:
                value = new_score
                best_move = col

            alpha = max(alpha, value)

            if alpha >= beta:
                break
        
        return (best_move, value, tree) if collect_tree else (best_move, value)

    else:
        value = float('inf')
        best_move = valid_moves[0]

        for col in valid_moves:
            new_board, row = game.transition_state(board, col, PLAYER_MIN)
            result = alpha_beta(new_board, depth - 1, alpha, beta, True, game, collect_tree)
            new_score = result[1]
            if collect_tree:
                tree['children'].append(result[2])

            if new_score < value:
                value = new_score
                best_move = col

            beta = min(beta, value)
            
            if alpha >= beta:
                break

        return (best_move, value, tree) if collect_tree else (best_move, value)


def print_tree(tree, prefix=""):
    """
    Print the tree structure in the terminal.
    """
    print(prefix + tree['label'])
    for child in tree['children']:
        print_tree(child, prefix + "  ")


def visualize_tree(board, depth, algorithm='minimax', game=None):
    """
    Visualize the search tree for minimax or alpha-beta in the terminal.
    """
    if game is None:
        game = ConnectFour()
    
    if algorithm == 'minimax':
        _, _, tree = minimax(board, depth, True, game, collect_tree=True)
    elif algorithm == 'alphabeta':
        _, _, tree = alpha_beta(board, depth, -float('inf'), float('inf'), True, game, collect_tree=True)
    
    print(f"{algorithm.upper()} Search Tree (Depth {depth}):")
    print_tree(tree)