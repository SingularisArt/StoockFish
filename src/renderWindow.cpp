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

void RenderWindow::cleanUp() {
  SDL_DestroyWindow(window);
}
