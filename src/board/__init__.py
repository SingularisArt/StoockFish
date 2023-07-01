import pygame

from .board import Board


def main():
    pygame.init()

    chess_board = Board()

    running = True
    chess_board.draw_board()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    chess_board.handle_mouse_click(pygame.mouse.get_pos())

    pygame.quit()


if __name__ == "__main__":
    main()
