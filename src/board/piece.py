import os

import pygame

from src.config import PIECE_IMG_LOCATION


class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.board_name = self.get_board_name()

        self.square_size = 0
        self.image = None

    def get_board_name(self):
        if self.name == "knight":
            initial_name = "N"
        elif self.name == "pawn":
            initial_name = self.name[0]
        else:
            initial_name = self.name[0].upper()

        return f"{self.color[0]}{initial_name}"

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

    def draw_piece(self, screen, col, row):
        screen.blit(
            self.image,
            (row * self.square_size, col * self.square_size),
        )

    def _get_legal_moves(self, board, row, col):
        _ = board
        _ = row
        _ = col
