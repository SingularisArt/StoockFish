/**
 * @file board.cpp
 * @author Hashem A. Damrah
 * @brief Chess board representation.
 * @copyright
 */

#include <bitset>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <sstream>

#include "./headers/board.h"

ChessBoard::ChessBoard(std::string fen) {
  // Set bitboards based on fen
  if (fen.empty()) {
    fen = fenPositions.at("startingPosition");
  }

  // Set bitboards based on fen
  loadFen(fen);
}

bool ChessBoard::loadFen(std::string fenString) {
  std::istringstream fenStream(fenString);
  std::string token;

  _clearBitBoards();

  U64 boardPos = 56;  // Fen string starts at a8 = index 56
  fenStream >> token;
  for (auto currChar : token) {
    switch (currChar) {
      case 'p':
        setBit(_pieces[BLACK][PAWN], boardPos++);
        break;
      case 'r':
        setBit(_pieces[BLACK][ROOK], boardPos++);
        break;
      case 'n':
        setBit(_pieces[BLACK][KNIGHT], boardPos++);
        break;
      case 'b':
        setBit(_pieces[BLACK][BISHOP], boardPos++);
        break;
      case 'q':
        setBit(_pieces[BLACK][QUEEN], boardPos++);
        break;
      case 'k':
        setBit(_pieces[BLACK][KING], boardPos++);
        break;
      case 'P':
        setBit(_pieces[WHITE][PAWN], boardPos++);
        break;
      case 'R':
        setBit(_pieces[WHITE][ROOK], boardPos++);
        break;
      case 'N':
        setBit(_pieces[WHITE][KNIGHT], boardPos++);
        break;
      case 'B':
        setBit(_pieces[WHITE][BISHOP], boardPos++);
        break;
      case 'Q':
        setBit(_pieces[WHITE][QUEEN], boardPos++);
        break;
      case 'K':
        setBit(_pieces[WHITE][KING], boardPos++);
        break;
      case '/':
        boardPos -= 16;  // Go down one rank
        break;
      default:boardPos += static_cast<U64>(currChar - '0');
    }
  }

  return true;
}

void ChessBoard::printBitboards() const {
  for (Color color : {WHITE, BLACK}) {
    for (PieceType pieceType : {PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING}) {
      std::cout
        << "Bitboard for " <<
        _colorToString(color) << " " <<
        _pieceTypeToString(pieceType) << ":" <<
        std::endl;;
      _printBitboard(_pieces[color][pieceType]);
      std::cout << std::endl;
    }
  }
}

void ChessBoard::displayBoard(RenderWindow window) const {
  // Render chessboard grid
  window.clean();

  for (int row = 0; row < 8; ++row) {
    for (int col = 0; col < 8; ++col) {
      if ((row + col) % 2 == 0) {
        ChessBoard::_displaySquare(window, 237, 214, 176, 0, row, col, 64);
      } else {
        ChessBoard::_displaySquare(window, 184, 135, 98, 0, row, col, 64);
      }
    }
  }

  // Render pieces
  for (Color color : {WHITE, BLACK}) {
    for (PieceType pieceType : {PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING}) {
      U64 bitboard = _pieces[color][pieceType];

      for (int squareIndex = 0; squareIndex < 64; ++squareIndex) {
        if (_getBit(bitboard, squareIndex)) {
          int row = squareIndex / 8;
          int col = squareIndex % 8;

          std::string filePath = "../assets/" + _colorToString(color) + "/" +
                                _pieceTypeToString(pieceType) + ".png";

          SDL_Texture *texture = window.loadTexture(filePath.c_str());
          SDL_Texture *scaledTexture =
              window.scaleTexture(texture, row, col, 64, 1);

          // Free the texture
          SDL_DestroyTexture(texture);
          SDL_DestroyTexture(scaledTexture);
        }
      }
    }
  }
}

int ChessBoard::_getBit(U64 bitboard, int index) const {
  return (bitboard & (1ULL << index)) ? 1 : 0;
}

void ChessBoard::_clearBitBoards() {
  for (Color color : {WHITE, BLACK}) {
    for (PieceType pieceType : {PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING}) {
      _pieces[color][pieceType] = ZERO;
    }
  }
}

void ChessBoard::_displaySquare(RenderWindow window, Uint8 r, Uint8 g, Uint8 b,
                                Uint8 a, int row, int col, int size) const {
  SDL_Rect square = {col * size, row * size, size, size};
  SDL_SetRenderDrawColor(window.renderer, r, g, b, a);
  SDL_RenderFillRect(window.renderer, &square);
}

std::vector<std::string> ChessBoard::_tokenizeString(const std::string& input,
                                                     char delimiter) {
  std::vector<std::string> tokens;
  std::istringstream tokenStream(input);
  std::string token;

  while (std::getline(tokenStream, token, delimiter)) {
    tokens.push_back(token);
  }

  return tokens;
}

std::string ChessBoard::_colorToString(Color color) const {
  return (color == WHITE) ? "white" : "black";
}

std::string ChessBoard::_pieceTypeToString(PieceType pieceType) const {
  switch (pieceType) {
    case PAWN:   return "pawn";
    case KNIGHT: return "knight";
    case BISHOP: return "bishop";
    case ROOK:   return "rook";
    case QUEEN:  return "queen";
    case KING:   return "king";
    default:     return "unknown";
  }
}

void ChessBoard::_printBitboard(U64 bitboard) const {
  for (int rank = 7; rank >= 0; --rank) {
    for (int file = 0; file < 8; ++file) {
      int squareIndex = rank * 8 + file;
      std::cout << std::bitset<1>(_getBit(bitboard, squareIndex)) << ' ';
    }
    std::cout << std::endl;
  }
}
