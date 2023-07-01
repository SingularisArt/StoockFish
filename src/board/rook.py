from .piece import Piece


class Rook(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "rook")

        self.color = color
        self.name = "rook"
        self.square_size = square_size

        self.starting_row = [0, 7]
        if color == "white":
            self.starting_col = 7
        elif color == "black":
            self.starting_col = 0

        self.image = self.get_image()
