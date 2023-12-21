// board.h
#ifndef BOARD_H
#define BOARD_H

#include <map>
#include <string>
#include <vector>

#include "./defs.h"

/**
 * @class ChessBoard.
 * @brief Represents a chess board.
 *
 * This class represents a chess board. Internally, each Board is represented
 * with 12, U64 bitboards. Each bitboard represents a different piece type and
 * color, as well as bitboards containing the occupancy, inverse of the
 * occupancy and en passant target square.
 */
class ChessBoard {
 public:
    /**
     * @brief Constructs a new board set to the specified fen string.
     *
     * @param fen Starting position of the board. If none is specified, the
     * default starting position is used.
     *
     */
    ChessBoard(std::string fen = "");

    /**
     * @brief Initialize board based on fen string.
     *
     * @param fen Fen String representing the board.
     */
    bool loadFen(std::string fenString);

    void printBitboards() const;

    // Hashmap for starting positions
    std::map<std::string, std::string> const fenPositions = {
      {"startingPosition",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"},
      {"emptyBoard", "8/8/8/8/8/8/8/8 w - -"},
      {"trickyPosition",
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1"},
      {"killerPosition",
        "rnbqkb1r/pp1p1pPp/8/2p1pP2/1P1P4/3P3P/P1P1P3/RNBQKBNR w KQkq e6 0 1"},
      {"cmkPosition",
        "r2q1rk1/ppp2ppp/2n1bn2/2b1p3/3pP3/3P1NPP/PPP1NPB1/R1BQ1RK1 b - - 0 9"},
    };

 private:
    U64 _pieces[2][6];

    void _clearBitBoards();

    std::vector<std::string> _tokenizeString(
        const std::string& input, char delimiter);

    int _getBit(U64 bitboard, int index) const;

    std::string _colorToString(Color color) const;

    std::string _pieceTypeToString(PieceType pieceType) const;

    void _printBitboard(U64 bitboard) const;
};

#endif  // BOARD_H
