from .piece import Piece


class Bishop(Piece):
    def __init__(self, color, square_size):
        super().__init__(color, "bishop")

        self.color = color
        self.name = "bishop"
        self.square_size = square_size

        self.get_image()

    def _get_legal_moves(self, board, row, col):
        legal_moves = []

        # Check the top left diagonal
        for i in range(1, 8):
            if row - i >= 0 and col - i >= 0:
                if board[row - i][col - i] == "--":
                    legal_moves.append((row - i, col - i))
                elif board[row - i][col - i][0] != self.color[0]:
                    legal_moves.append((row - i, col - i))
                    break
                else:
                    break
            else:
                break

        # Check the top right diagonal
        for i in range(1, 8):
            if row - i >= 0 and col + i <= 7:
                if board[row - i][col + i] == "--":
                    legal_moves.append((row - i, col + i))
                elif board[row - i][col + i][0] != self.color[0]:
                    legal_moves.append((row - i, col + i))
                    break
                else:
                    break
            else:
                break

        # Check the bottom left diagonal
        for i in range(1, 8):
            if row + i <= 7 and col - i >= 0:
                if board[row + i][col - i] == "--":
                    legal_moves.append((row + i, col - i))
                elif board[row + i][col - i][0] != self.color[0]:
                    legal_moves.append((row + i, col - i))
                    break
                else:
                    break
            else:
                break

        # Check the bottom right diagonal
        for i in range(1, 8):
            if row + i <= 7 and col + i <= 7:
                if board[row + i][col + i] == "--":
                    legal_moves.append((row + i, col + i))
                elif board[row + i][col + i][0] != self.color[0]:
                    legal_moves.append((row + i, col + i))
                    break
                else:
                    break
            else:
                break

        return legal_moves
