/**
 * @file
 * @author Hashem A. Damrah
 * @brief Main file for the chess engine.
 * @copyright
 */

#include "./headers/board.h"

#include <iostream>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

int main(int argc, char* args[]) {
  // Initialize SDL
  if (SDL_Init(SDL_INIT_EVERYTHING) > 0) {
    std::cerr
      << "SDL could not initialize! SDL_Error: "
      << SDL_GetError()
      << std::endl;
  }

  // Initialize SDL_image
  if (!(IMG_Init(IMG_INIT_PNG))) {
    std::cerr
      << "SDL_image could not initialize! SDL_image Error: "
      << SDL_GetError()
      << std::endl;
  }

  ChessBoard chessBoard;
  // chessBoard.printBitboards();

  return 0;
}
