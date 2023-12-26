/**
 * @file renderWindow.cpp
 * @author Hashem A. Damrah
 * @brief Implementation file for the RenderWindow class.
 * @copyright
 */

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

#include <iostream>

#include "./headers/renderWindow.h"

RenderWindow::RenderWindow(const char *title, int p, int h)
    : window(NULL), renderer(NULL) {
  window = SDL_CreateWindow(title, SDL_WINDOWPOS_UNDEFINED,
                            SDL_WINDOWPOS_UNDEFINED, p, h, SDL_WINDOW_SHOWN);

  if (window == NULL) {
    std::cerr << "Window failed to init. Error: " << SDL_GetError()
              << std::endl;
  }

  renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
}

SDL_Texture *RenderWindow::loadTexture(const char *filePath) {
  SDL_Texture *texture = NULL;
  texture = IMG_LoadTexture(renderer, filePath);

  if (texture == NULL) {
    std::cerr << "Failed to load texture. Error: " << SDL_GetError()
              << std::endl;
  }

  return texture;
}

void RenderWindow::cleanUp() { SDL_DestroyWindow(window); }

void RenderWindow::clean() { SDL_RenderClear(renderer); }

void RenderWindow::render(SDL_Texture *texture, int row, int col) {
  int squareSize = 32;
  int x = col * squareSize;
  int y = row * squareSize;

  // Create a destination rectangle to specify where to render the texture.
  SDL_Rect destRect = {x, y, squareSize, squareSize};

  // Render the texture to the specified destination rectangle.
  SDL_RenderCopy(renderer, texture, NULL, &destRect);

  // Update the screen.
  SDL_RenderPresent(renderer);
}

SDL_Texture *RenderWindow::scaleTexture(SDL_Texture *texture, int row, int col,
                                        int size, double scale) {
  // Calculate the destination rectangle for scaling
  int x = col * size;
  int y = row * size;

  int scaledWidth = static_cast<int>(size * scale);
  int scaledHeight = static_cast<int>(size * scale);

  // Create a surface to render the scaled texture onto
  SDL_Surface *surface =
      SDL_CreateRGBSurface(0, scaledWidth, scaledHeight, 32, 0, 0, 0, 0);

  // Create a destination rectangle for rendering
  SDL_Rect destRect = {x, y, scaledWidth, scaledHeight};  // Adjusted for position

  // Create a texture from the surface
  SDL_Texture *scaledTexture = SDL_CreateTextureFromSurface(renderer, surface);

  // Render the texture to the surface
  SDL_RenderCopy(renderer, texture, NULL, &destRect);

  // Free the surface
  SDL_FreeSurface(surface);

  // Return the scaled texture
  return scaledTexture;
}
void RenderWindow::display() { SDL_RenderPresent(renderer); }
