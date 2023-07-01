import pygame

from .king import King
from .queen import Queen
from .rook import Rook
from .bishop import Bishop
from .knight import Knight
from .pawn import Pawn


class Board:
    def __init__(self):
        self.width = 640
        self.height = 640
        self.board_size = 8
        self.square_size = self.width // self.board_size
        self.colors = [
            (240, 217, 181),
            (181, 136, 99),
        ]
        self.board = [[None] * self.board_size for _ in range(self.board_size)]

        self.selected_piece = None
        self.legal_moves = []

        self.pieces = {
            "white": {
                "king": King("white", self.square_size),
                "queen": Queen("white", self.square_size),
                "rook": Rook("white", self.square_size),
                "bishop": Bishop("white", self.square_size),
                "knight": Knight("white", self.square_size),
                "pawn": Pawn("white", self.square_size),
            },
            "black": {
                "king": King("black", self.square_size),
                "queen": Queen("black", self.square_size),
                "rook": Rook("black", self.square_size),
                "bishop": Bishop("black", self.square_size),
                "knight": Knight("black", self.square_size),
                "pawn": Pawn("black", self.square_size),
            },
        }

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chess Board")

    def initialize_pieces(self):
        for color in self.pieces.values():
            for piece in color.values():
                piece.initalize_piece(self.screen)

    def place_piece(self, piece, row, col):
        piece.draw_piece(
            self.screen,
            row * self.square_size,
            col * self.square_size,
        )

    def get_piece_at_square(self, row, col):
        return self.board[row][col]

    def handle_mouse_click(self, mouse_pos):
        row = mouse_pos[1] // self.square_size
        col = mouse_pos[0] // self.square_size

        if self.selected_piece is None:
            piece = self.get_piece_at_square(row, col)
            if piece is not None:
                self.selected_piece = piece
                self.legal_moves = self.selected_piece.get_legal_moves(
                    self.board,
                )
        else:
            if (row, col) in self.legal_moves:
                self.move_piece(self.selected_piece, row, col)
                self.selected_piece = None
                self.legal_moves = []

    def move_piece(self, piece, row, col):
        current_row, current_col = piece.get_position()
        self.board[current_row][current_col] = None
        self.board[row][col] = piece
        piece.set_position(row, col)

    def draw_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                square_color = self.colors[(row + col) % 2]
                pygame.draw.rect(
                    self.screen,
                    square_color,
                    (
                        col * self.square_size,
                        row * self.square_size,
                        self.square_size,
                        self.square_size,
                    ),
                )

                if (row, col) in self.legal_moves:
                    highlight_color = (0, 255, 0)
                    pygame.draw.rect(
                        self.screen,
                        highlight_color,
                        (
                            col * self.square_size,
                            row * self.square_size,
                            self.square_size,
                            self.square_size,
                        ),
                    )

        self.initialize_pieces()

        pygame.display.flip()

    def update_board(self):
        self.draw_board()
