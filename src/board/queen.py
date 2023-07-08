from .piece import Piece


class Queen(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "queen")

        self.color = color
        self.name = "queen"
        self.square_size = square_size

        self.get_image()

    def _get_legal_moves(self, board, row, col):
        legal_moves = []

        # Check in all eight directions: up, down, left, right, and diagonals
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        for direction in directions:
            delta_row, delta_col = direction
            new_row, new_col = row + delta_row, col + delta_col

            while 0 <= new_row < 8 and 0 <= new_col < 8:
                destination = board[new_row][new_col]

                if destination == "--":
                    legal_moves.append((new_row, new_col))
                elif destination[0] != self.color[0]:
                    legal_moves.append((new_row, new_col))
                    break
                else:
                    break

                new_row += delta_row
                new_col += delta_col

        return legal_moves
