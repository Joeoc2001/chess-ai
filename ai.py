import random
import chess


def make_move(board: chess.Board, time_remaining: float) -> str:
    """
    `board` gives the current board state from which you should make your move.
    See https://python-chess.readthedocs.io/en/v1.4.0/ for full documentation,
    or below for some example usage.

    `time_remaining` gives the number of seconds left on your chess clock.
    You should return a uci-formatted move representing the move that your AI
    wishes to make.

    For example, to move your pawn from e2 to e4, you should return the string 'e2e4'.

    If you make an invalid move, or if your chess clock times out, you forfeit the game.

    Note that you are passed a copy of the board object, so methods such as `board.reset()`
    will not change the master copy, only your local version.
    """

    # Get some interesting information
    legal_moves = list(board.legal_moves)

    best_move = None
    best_type = 0
    for move in legal_moves:
        t = board.piece_type_at(move.to_square)
        if t is not None and t > best_type:
            best_move = move
            best_type = t
    if best_move is None:
        best_move = random.choice(legal_moves)

    # Return the code of the move
    return best_move.uci()
