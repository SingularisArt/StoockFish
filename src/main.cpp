/**
 * @file main.cpp
 * @author Hashem A. Damrah
 * @brief Main file for the chess engine.
 * @copyright
 */

#include "./headers/board.h"
#include "./headers/renderWindow.h"

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

  /**
   * @brief The window that the game is rendered in.
   */
  RenderWindow window("Chess", 700, 700);

  /**
   * @brief The event that is used to handle user input.
   */
  SDL_Event event;

  /**
   * @brief Variable that controls the main loop.
   */
  bool isRunning = true;

  /**
   * @brief The chess board.
   */
  ChessBoard chessBoard;
  // chessBoard.printBitboards();

  // Main game loop
  while (isRunning) {
    // Check for user input
    while (SDL_PollEvent(&event)) {
      // Check if the user wants to quit
      if (event.type == SDL_QUIT) {
        // If so, exit the main loop
        isRunning = false;
      }
    }
  }

  window.cleanUp();
  SDL_Quit();

  return 0;
}
