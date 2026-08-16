import consts
import random

field = []

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


clear_field()
print(field)





