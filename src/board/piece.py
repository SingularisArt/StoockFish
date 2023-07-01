import os

import pygame

from src.config import PIECE_IMG_LOCATION


class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

        self.square_size = 0
        self.image = None

        self.row = None
        self.col = None

        self.starting_row = 0
        self.starting_col = 0

    def get_image(self):
        self.image = pygame.image.load(
            os.path.join(
                PIECE_IMG_LOCATION,
                self.color,
                f"{self.name}.png",
            )
        )
        self.image = pygame.transform.scale(
            self.image,
            (
                self.square_size,
                self.square_size,
            ),
        )

        return self.image

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def initalize_piece(self, screen):
        if isinstance(self.starting_row, list):
            for row in self.starting_row:
                self.draw_piece(screen, row, self.starting_col)
        else:
            self.draw_piece(screen, self.starting_row, self.starting_col)

    def draw_piece(self, screen, row, col):
        screen.blit(
            self.image,
            (row * self.square_size, col * self.square_size),
        )

    def get_legal_moves(self, board):
        raise NotImplementedError(
            f"Subclass must implement get_legal_moves method with {board}",
        )

    def draw_legal_moves(self, screen, square_size):
        raise NotImplementedError(
            f"Subclass must implement draw_legal_moves method with {screen}, {square_size}"
        )
