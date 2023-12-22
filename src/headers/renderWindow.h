/**
 * @file renderWindow.h
 * @author Hashem A. Damrah
 * @brief Header file for the RenderWindow class.
 * @copyright
 */

#pragma once
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

/**
 * @class RenderWindow
 * @brief A class that represents the window that the game is rendered in.
 *
 */
class RenderWindow {
 public:
    /**
     * @brief Construct a new Render Window object.
     *
     * @param title The title of the window.
     * @param w Width of the window.
     * @param h Height of the window.
     */
    RenderWindow(const char* title, int w, int h);

    /**
     * @brief Render the game.
     *
     * @param filePath The path to the image that is to be rendered.
     * @return SDL_Texture* The texture that is to be rendered.
     */
    SDL_Texture* loadTexture(const char* filePath);

    /**
     * @brief Destroy the Render Window object.
     */
    void cleanUp();

 private:
    /**
     * @brief The window that the game is rendered in.
     */
    SDL_Window* window;

    /**
     * @brief The renderer that renders the game.
     */
    SDL_Renderer* renderer;
};
