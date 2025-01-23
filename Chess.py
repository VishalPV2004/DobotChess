import cv2

image = cv2.imread("chessB.png")
clone = image.copy()

white_pieces = {
    "w1": (38, 596), "w2": (121, 595), "w3": (200, 594), "w4": (277, 594),
    "w5": (357, 595), "w6": (435, 593), "w7": (520, 594), "w8": (599, 592),
    "w16": (36, 514), "w15": (119, 514), "w14": (197, 514), "w13": (278, 515),
    "w12": (356, 514), "w11": (437, 516), "w10": (517, 514), "w9": (596, 514)
}

black_pieces = {
    "b1": (41, 36), "b2": (121, 35), "b3": (197, 37), "b4": (279, 36),
    "b5": (358, 35), "b6": (438, 37), "b7": (517, 37), "b8": (597, 37),
    "b16": (38, 118), "b15": (121, 117), "b14": (197, 118), "b13": (278, 117),
    "b12": (357, 118), "b11": (437, 118), "b10": (517, 118), "b9": (599, 116)
}

piece_map = {
    "white rook 1": "w1", "white knight 1": "w2", "white bishop 1": "w3", "white queen": "w4",
    "white king": "w5", "white bishop 2": "w6", "white knight 2": "w7", "white rook 2": "w8",
    "white pawn 1": "w16", "white pawn 2": "w15", "white pawn 3": "w14", "white pawn 4": "w13",
    "white pawn 5": "w12", "white pawn 6": "w11", "white pawn 7": "w10", "white pawn 8": "w9",
    "black rook 1": "b1", "black knight 1": "b2", "black bishop 1": "b3", "black queen": "b4",
    "black king": "b5", "black bishop 2": "b6", "black knight 2": "b7", "black rook 2": "b8",
    "black pawn 1": "b16", "black pawn 2": "b15", "black pawn 3": "b14", "black pawn 4": "b13",
    "black pawn 5": "b12", "black pawn 6": "b11", "black pawn 7": "b10", "black pawn 8": "b9"
}

def draw_pieces(image, pieces, color):
    for (x, y) in pieces.values():
        cv2.circle(image, (x, y), 7, color, -1)

draw_pieces(clone, white_pieces, (0, 255, 0))
draw_pieces(clone, black_pieces, (255, 0, 0))

occupied_positions = set()

while True:
    cv2.imshow("Chessboard", clone)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

    user_input = input("Enter piece name (or 'exit' to stop): ").lower()

    if user_input == "exit":
        break

    if user_input in piece_map:
        piece_key = piece_map[user_input]
        position = white_pieces.get(piece_key) or black_pieces.get(piece_key)

        if position in occupied_positions:
            print("Already occupied")
        else:
            occupied_positions.add(position)
            cv2.circle(clone, position, 10, (0, 0, 255), -1)
    else:
        print("Invalid input. Try again.")

cv2.destroyAllWindows()
