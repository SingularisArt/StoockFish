/**
 * @file
 * @author Hashem A. Damrah
 * @brief Useful definitions.
 */

#define setBit(bitboard, square) (bitboard |= (ONE << square))

typedef unsigned long long U64;

enum Color {
  WHITE,
  BLACK,
};

enum PieceType {
  PAWN,
  KNIGHT,
  BISHOP,
  ROOK,
  QUEEN,
  KING,
};

/**
 * @brief An empty bitboard. (ie. the number 0)
 */
const U64 ZERO = U64(0);

/**
 * @brief A bitboard containing only the square a1. (ie. the number 1)
 */
const U64 ONE = U64(1);
