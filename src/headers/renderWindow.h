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
     * @brief The window that the game is rendered in.
     */
    SDL_Window* window;

    /**
     * @brief The renderer that renders the game.
     */
    SDL_Renderer* renderer;

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
    SDL_Texture* loadTexture(const char *filePath);

    /**
     * @brief Destroy the Render Window object.
     */
    void cleanUp();

    /**
     * @brief Clear the window.
     */
    void clean();

    /**
     * @brief Render the texture.
     *
     * @param texture The texture that is to be rendered.
     * @param row The row that the texture is to be rendered in.
     * @param col The column that the texture is to be rendered in.
     */
    void render(SDL_Texture *texture, int row, int col);

    /**
     * @brief Scale the texture, render it, and return it.
     *
     * @param texture The texture that is to be scaled.
     * @param row The row that the texture is to be scaled in.
     * @param col The column that the texture is to be scaled in.
     * @param size The size of the texture.
     * @param scale The scale of the texture.
     */
    SDL_Texture *scaleTexture(SDL_Texture *texture, int row, int col, int size,
                              double scale);

    /**
     * @brief Display the game.
     */
    void display();
};
