WINDOW_HEIGHT = 800
WINDOW_WIDTH = 400

WHITE = (252, 252, 252)
BLACK = (0, 0, 0)
DARK_GREEN = (2, 28, 19)
LINES_GREEN = (7, 77, 52)
GRASS_GREEN = (6, 99, 6)

ROW_NUM = 25
COLUMN_NUM = 50

SQUARE_SIZE = 16

SOLDIER = "soldier"
LANDMINE = "landmine"
EMPTY = "empty"
FLAG = "flag"
BUSH = "bush"

OPTIONS = [LANDMINE, EMPTY]
options = OPTIONS.copy()

FLAG_INDEX = [(21,46), (21,47), (21,48), (21,49),
              (22,46), (22,47), (22,48), (22,49),
              (23,46), (23,47), (23,48), (23,49),]

GAME = 1
WIN = 2
LOSE = 3