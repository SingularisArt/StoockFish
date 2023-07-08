from .piece import Piece


class King(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "king")

        self.color = color
        self.name = "king"
        self.square_size = square_size

        self.get_image()

    def _get_legal_moves(self, board, row, col):
        legal_moves = []
        color = self.color[0]

        # Define the offsets for pawn movements
        offsets = [
            (1, 0),
            (1, 1),
            (1, -1),
            (0, 1),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (-1, 1),
        ]

        for offset in offsets:
            target_row = row + offset[0]
            target_col = col + offset[1]

            try:
                target_square = board[target_row][target_col]

                if target_square == "--" or target_square[0] != color:
                    legal_moves.append((target_row, target_col))
            except IndexError:
                continue

        return legal_moves
