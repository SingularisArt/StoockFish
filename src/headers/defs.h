/**
 * @file board.h
 * @author Hashem A. Damrah
 * @brief Useful definitions.
 * @copyright
 */

#define setBit(bitboard, square) (bitboard |= (ONE << square))

typedef unsigned long long U64;

/**
 * @brief The color of a piece.
 */
enum Color {
  WHITE,
  BLACK,
};

/**
 * @brief The type of a piece.
 */
enum PieceType {
  PAWN,
  KNIGHT,
  BISHOP,
  ROOK,
  QUEEN,
  KING,
};

/**
 * @brief An in-active square. (ie. the number 0)
 */
const U64 ZERO = U64(0);

/**
 * @brief An active square. (ie. the number 1)
 */
const U64 ONE = U64(1);
