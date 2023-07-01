from .piece import Piece


class Pawn(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "pawn")

        self.color = color
        self.name = "pawn"
        self.square_size = square_size

        self.starting_row = [i for i in range(8)]

        if color == "white":
            self.starting_col = 6
        elif color == "black":
            self.starting_col = 1

        self.image = self.get_image()
