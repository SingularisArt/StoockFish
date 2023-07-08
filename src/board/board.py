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

        self.checkmate = False
        self.stalemate = False
        self.in_check = False
        self.pins = []
        self.checks = []
        self.enpassant_possible = ()
        self.enpassant_possible_log = [self.enpassant_possible]
        self.current_castling_rights = CastleRights(True, True, True, True)
        self.castle_rights_log = [
            CastleRights(
                self.current_castling_rights.wks,
                self.current_castling_rights.bks,
                self.current_castling_rights.wqs,
                self.current_castling_rights.bqs,
            )
        ]

        self.board_backend = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.board = [[None] * self.board_size for _ in range(self.board_size)]

        self.current_color_turn = "white"
        self.selected_piece = None
        self.legal_moves = []

        self.pieces = {
            "white": {
                "K": King("white", self.square_size),
                "Q": Queen("white", self.square_size),
                "R": Rook("white", self.square_size),
                "B": Bishop("white", self.square_size),
                "N": Knight("white", self.square_size),
                "p": Pawn("white", self.square_size),
            },
            "black": {
                "K": King("black", self.square_size),
                "Q": Queen("black", self.square_size),
                "R": Rook("black", self.square_size),
                "B": Bishop("black", self.square_size),
                "N": Knight("black", self.square_size),
                "p": Pawn("black", self.square_size),
            },
        }

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.piece_surface = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA,
        )
        self.square_surface = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA,
        )

    def initialize_pieces(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                piece = self.board_backend[row][col]
                if piece != "--":
                    color = "white" if piece[0] == "w" else "black"
                    piece = self.pieces[color][piece[1]]
                    piece.draw_piece(self.piece_surface, row, col)

    def get_piece_at_square(self, row, col):
        return self.board_backend[row][col]

    def handle_mouse_click(self, mouse_pos):
        row = mouse_pos[1] // self.square_size
        col = mouse_pos[0] // self.square_size

        if self.selected_piece is None:
            piece = self.get_piece_at_square(row, col)
            if (piece[0] == "w" and self.current_color_turn == "white") or (
                piece[0] == "b" and self.current_color_turn == "black"
            ):
                self.cur_row = row
                self.cur_col = col

                self.selected_piece = self.pieces[self.current_color_turn][piece[1]]

                self.legal_moves = self.selected_piece._get_legal_moves(
                    self.board_backend,
                    row,
                    col,
                )

                if self.legal_moves == []:
                    self.selected_piece = None

                self.draw_legal_squares(
                    self.legal_moves,
                    row,
                    col,
                )
        elif self.legal_moves:
            if (row, col) in self.legal_moves:
                self.move_piece(
                    self.selected_piece, self.cur_row, self.cur_col, row, col
                )

                if self.current_color_turn == "white":
                    self.current_color_turn = "black"
                else:
                    self.current_color_turn = "white"

            self.selected_piece = None
            self.draw_board()

    def move_piece(self, piece, cur_row, cur_col, new_row, new_col):
        self.board_backend[cur_row][cur_col] = "--"
        self.board_backend[new_row][new_col] = piece.board_name

        pygame.draw.rect(
            self.piece_surface,
            (0, 0, 0, 0),
            (
                cur_col * self.square_size,
                cur_row * self.square_size,
                self.square_size,
                self.square_size,
            ),
        )

        self.draw_board()

    def draw_board(self):
        self.clear_surfaces()

        for row in range(self.board_size):
            for col in range(self.board_size):
                square_color = self.colors[(row + col) % 2]
                pygame.draw.rect(
                    self.square_surface,
                    square_color,
                    (
                        col * self.square_size,
                        row * self.square_size,
                        self.square_size,
                        self.square_size,
                    ),
                )

        self.initialize_pieces()

    def draw_legal_squares(self, moves, cur_col, cur_row):
        if not moves:
            return

        for move in moves:
            row, col = move

            center_x = (col + 0.5) * self.square_size
            center_y = (row + 0.5) * self.square_size

            radius = self.square_size // 6
            color = (255, 255, 255)

            # Draw the circle on the screen
            pygame.draw.circle(
                self.piece_surface,
                color,
                (center_x, center_y),
                radius,
            )

        x = cur_row
        y = cur_col

        light_square = (247, 235, 88)
        dark_square = (220, 182, 49)
        square_color = dark_square if (x + y) % 2 == 1 else light_square

        # Make the current square a different color
        pygame.draw.rect(
            self.square_surface,
            square_color,
            (
                x * self.square_size,
                y * self.square_size,
                self.square_size,
                self.square_size,
            ),
        )

    def clear_surfaces(self):
        self.piece_surface = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA,
        )
        self.square_surface = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA,
        )

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.square_surface, (0, 0))
        self.screen.blit(self.piece_surface, (0, 0))
        pygame.display.flip()
