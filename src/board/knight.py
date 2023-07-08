from .piece import Piece


class Knight(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "knight")

        self.color = color
        self.name = "knight"
        self.square_size = square_size

        self.get_image()

    def _get_legal_moves(self, board, row, col):
        legal_moves = []

        # Possible knight moves relative to its current position
        knight_moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]

        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                destination = board[new_row][new_col]

                if destination == "--" or destination[0] != self.color[0]:
                    legal_moves.append((new_row, new_col))

        return legal_moves
