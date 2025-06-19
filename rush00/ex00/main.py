def checkmate(board):
    """
    Check if the king is in check on the given chessboard.
    
    Args:
        board (str): A string representing the chessboard with rows separated by newlines
        
    Returns:
        None: Prints "Success" if king is in check, "Fail" otherwise
    """
    try:
        # Split the board into rows
        rows = board.split('\n')
        
        # Find the position of the King (K)
        king_pos = None
        for i, row in enumerate(rows):
            if 'K' in row:
                king_pos = (i, row.index('K'))
                break
        
        if not king_pos:
            print("Fail")
            return
        
        king_row, king_col = king_pos
        
        # Check for each piece type if it can attack the king
        for i, row in enumerate(rows):
            for j, piece in enumerate(row):
                if piece == 'P':  # Pawn
                    # Pawns attack diagonally forward
                    if (i == king_row + 1 and 
                        (j == king_col - 1 or j == king_col + 1)):
                        print("Success")
                        return
                
                elif piece == 'R':  # Rook
                    # Check same row or column
                    if i == king_row or j == king_col:
                        # Check if path is clear
                        if i == king_row:  # Same row
                            step = 1 if j < king_col else -1
                            for col in range(j + step, king_col, step):
                                if rows[i][col] != '.':
                                    break
                            else:
                                print("Success")
                                return
                        else:  # Same column
                            step = 1 if i < king_row else -1
                            for row_idx in range(i + step, king_row, step):
                                if rows[row_idx][j] != '.':
                                    break
                            else:
                                print("Success")
                                return
                
                elif piece == 'B':  # Bishop
                    # Check diagonals
                    if abs(i - king_row) == abs(j - king_col):
                        # Check if path is clear
                        row_step = 1 if i < king_row else -1
                        col_step = 1 if j < king_col else -1
                        steps = abs(i - king_row)
                        for step in range(1, steps):
                            if rows[i + row_step * step][j + col_step * step] != '.':
                                break
                        else:
                            print("Success")
                            return
                
                elif piece == 'Q':  # Queen
                    # Check rook-like and bishop-like moves
                    if i == king_row or j == king_col:  # Rook move
                        if i == king_row:  # Same row
                            step = 1 if j < king_col else -1
                            for col in range(j + step, king_col, step):
                                if rows[i][col] != '.':
                                    break
                            else:
                                print("Success")
                                return
                        else:  # Same column
                            step = 1 if i < king_row else -1
                            for row_idx in range(i + step, king_row, step):
                                if rows[row_idx][j] != '.':
                                    break
                            else:
                                print("Success")
                                return
                    elif abs(i - king_row) == abs(j - king_col):  # Bishop move
                        row_step = 1 if i < king_row else -1
                        col_step = 1 if j < king_col else -1
                        steps = abs(i - king_row)
                        for step in range(1, steps):
                            if rows[i + row_step * step][j + col_step * step] != '.':
                                break
                        else:
                            print("Success")
                            return
        
        # If no pieces can attack the king
        print("Fail")
    
    except Exception:
        # Handle any unexpected errors gracefully
        print("Fail")


# Example main.py implementation
def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
