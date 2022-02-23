import random
import pyautogui
from PIL import Image
import time

# import easyocr
import numpy as np


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.card = f"{self.number:02d}" + self.suit
        self.color = "RED" if self.suit in ("S", "C") else "BLACK"


def create_deck(joker=False):
    deck = [Card(j, i) for i in range(1, 14) for j in "SCHD"]
    if joker:
        pass  # TODO: add jokers
    random.shuffle(deck)
    return deck


def screen_capture():
    time.sleep(5)
    image = pyautogui.screenshot()
    x_start, y_start = 222, 560
    x_size, y_size = 42, 70
    x_step, y_step = 297, 82

    x0 = int(x_start)
    for i in [2, 2]:  # [7] * 4 + [6] * 4:
        y0 = int(y_start)
        for _ in range(i):
            im = image.crop((x0, y0, x0 + x_size, y0 + y_size))
            im.save("temp.jpg")
            im.show()
            # result = easyocr.Reader(["en"], gpu=False).readtext("temp.jpg")
            # print(result)
            print(get_color(im))

            y0 += y_step
        x0 += x_step


def get_color(im):
    imArray = np.array(im).tolist()
    with open(
        "text" + str(random.randint(1, 25)) + ".txt", "w+", newline="\n"
    ) as outfile:
        for i in imArray:
            for j in i:
                outfile.write(f"{j[0]:03d}_{j[1]:03d}_{j[2]:03d}\n")
                if (j[0], j[1], j[2]) == (0, 0, 0):
                    return "Black!"
    return "Red!"


def print_table(columns, trans, piles):
    for i in trans + piles:
        print(i + " ", end="")
    print("\n")
    max_col_size = max([len(i) for i in columns])
    for i in range(max_col_size):
        for col in columns:
            if i < len(col):
                print(col[i].card + " ", end="")
        print()


def main():
    deck = create_deck()
    trans = ["000"] * 4
    piles = ["000"] * 4
    columns = []
    table = (columns, trans, piles)
    s = 0
    for q in [7] * 4 + [6] * 4:
        columns.append(deck[s : s + q])
        s += int(q)

    print_table(columns, trans, piles)


# main()
screen_capture()
