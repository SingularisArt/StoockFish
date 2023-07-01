import argparse

from src.board import main as board_main


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--train",
        action="store_true",
        default=True,
        help="Train the chess engine.",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        default=False,
        help="Validate the chess engine.",
    )
    parser.add_argument(
        "--play",
        choices=["human", "engine"],
        help="Play some chess.",
    )

    args = parser.parse_args()

    board_main()

    if args.train:
        print("Training the chess engine.")
    elif args.validate:
        print("Validating the chess engine.")
    elif args.play:
        print("Playing some chess.")


if __name__ == "__main__":
    main()
