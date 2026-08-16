import consts
import random

field = []
bush_field = []

def clear_field():
    global field
    empty_index = []
    for i in range(consts.ROW_NUM):
        row = []

        for j in range(consts.COLUMN_NUM):
            if (j == 0) and (i == 0):
                square = {"status": consts.SOLDIER, "x": j, "y": i}

            elif not flag_place(i, j):
                square = {"status": consts.EMPTY, "x": j, "y": i}
                empty_index.append((i, j))

            else:
                square = {"status": consts.FLAG, "x": j, "y": i}

            row.append(square)
        field.append(row)

    add_landmines(empty_index)



def flag_place(i, j):
    if (i,j) in consts.FLAG_INDEX:
        return True
    else:
        return False


def add_landmines(index_list):
    landmine_count = 0
    while landmine_count < 20:
        random_index = random.choice(index_list)
        if (field[random_index[0]][random_index[1]]["status"] == consts.EMPTY) and (random_index[1] < consts.COLUMN_NUM - 3):
            for i in range(3):
                field[random_index[0]][random_index[1] + i]["status"] = consts.LANDMINE
            landmine_count += 1


def grass_field():
    global bush_field
    for i in range(consts.ROW_NUM):
        row = []

        for j in range(consts.COLUMN_NUM):
            square = {"status": consts.EMPTY, "x": j, "y": i}

            row.append(square)
        bush_field.append(row)

    add_bushes()


def add_bushes():
    count = 0
    while count < 20:
        random_row = random.randint(0, consts.ROW_NUM - 1)
        random_column = random.randint(0, consts.COLUMN_NUM - 1)
        if place_bush(random_row, random_column):
            bush_field[random_row][random_column]["status"] = consts.BUSH
            count += 1


def place_bush(row, column):
    if ((row,column) not in consts.FLAG_INDEX) and (bush_field[row][column]["status"] == consts.EMPTY) and (column < consts.COLUMN_NUM - 2):
        return True
    return False


clear_field()
print(field)

grass_field()
print(bush_field)

count = 0
for i in range(consts.ROW_NUM):
    for j in range(consts.COLUMN_NUM):
        if bush_field[i][j]["status"] == consts.BUSH:
            count += 1

print(count)






