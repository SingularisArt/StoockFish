from .piece import Piece


class Pawn(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "pawn")

        self.color = color
        self.name = "pawn"
        self.square_size = square_size

        self.get_image()

    def _get_legal_moves(self, board, row, col):
        legal_moves = []

        # White moves
        if self.color == "white":
            # Check if the square in front of us is empty
            if board[row - 1][col] == "--":
                legal_moves.append((row - 1, col))

            # Check if we are on the starting position
            if row == 6 and board[row - 2][col] == "--":
                legal_moves.append((row - 2, col))

            # Check if there is a black piece diagonally to the left
            if col != 0:
                if board[row - 1][col - 1][0] == "b":
                    legal_moves.append((row - 1, col - 1))

            # Check if there is a black piece diagonally to the right
            if col != 7:
                if board[row - 1][col + 1][0] == "b":
                    legal_moves.append((row - 1, col + 1))

        # Black moves
        else:
            # Check if the square in front of us is empty
            if board[row + 1][col] == "--":
                legal_moves.append((row + 1, col))

            # Check if we are on the starting position
            if row == 1 and board[row + 2][col] == "--":
                legal_moves.append((row + 2, col))

            # Check if there is a white piece diagonally to the left
            if col != 0:
                if board[row + 1][col - 1][0] == "w":
                    legal_moves.append((row + 1, col - 1))

            # Check if there is a white piece diagonally to the right
            if col != 7:
                if board[row + 1][col + 1][0] == "w":
                    legal_moves.append((row + 1, col + 1))

        return legal_moves
