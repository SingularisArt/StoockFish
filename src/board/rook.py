from .piece import Piece


class Rook(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "rook")

        self.color = color
        self.name = "rook"
        self.square_size = square_size

        self.get_image()

    def _get_legal_moves(self, board, row, col):
        legal_moves = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
