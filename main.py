import random
import os
import time

#======================GAME FUNCTION======================#
def clean_s() -> None:
    time.sleep(0)
    os.system('CLS')

def print_arr(arr):
    for i in range(sizeA):
        if i == 0:
            print("   ", end=' ')
        elif i == sizeA - 1:
            print("(Y)", end=' ')
        else:
            print(" ", (sizeA - 1) - i, end=' ')
        for j in range(sizeA):
            print(arr[i][j], end='  ')
        print()
        if i == sizeA - 1:
            print("   ", end='')
            for n in range(sizeA - 1):
                if n == 0:
                    print("(X) ", end='')
                else:
                    print(n, end='  ')
            print()

def print_data1():
    print("\tGame \"Serpentine\"")
    print("\tmatrix size {} x {}".format(sizeA - 2, sizeA - 2))

def print_data2(level_cur, enemy_num_cur):
    print("Data:")
    print("\tGame level\t-> ", level_cur)
    print("\tEnemy qty\t-> ", enemy_num_cur)

def fill_arr(arr):
    for i in range(sizeA):
        temp = []
        if i == 0 or i == sizeA - 1:
            for j in range(sizeA):
                temp.append("*")
        else:
            for j in range(sizeA):
                if j == 0 or j == sizeA - 1:
                    temp.append("*")
                else:
                    temp.append(" ")
        arr.append(temp)

    return arr

def clear_track(arr):
    for i in range(sizeA):
        for j in range(sizeA):
            if arr[i][j] != '@' and arr[i][j] != '*' and arr[i][j] != '+':
                arr[i][j] = ' '

def fill_enemy(arr, level_game):
    x2: int # enemies coordinates
    y2: int # enemies coordinates
    ind = level_game
    arr_enemy = []
    x_player, y_player = pos_player(arr)

    for i in range(level_game):
        while True:
            logic = True
            arr_temp = []

            y2 = random.randrange(1, 8)
            arr_temp.append(y2)

            x2 = random.randrange(1, 8)
            arr_temp.append(x2)

            if arr[y2][x2] == '@' or arr[y2][x2] == '+':
                continue
            elif x2 == x_player or y2 == y_player:
                continue

            for k in range(level_game - ind):
                if y2 == arr_enemy[k][0] or x2 == arr_enemy[k][1]:
                    logic = False
                    break

            if logic:
                arr_enemy.append(arr_temp)
                ind -= 1
                break

        arr[x2][y2] = '+'

    return clear_track(arr)

def check_enemy(arr):
    for i in arr:
        for j in i:
            if j == '+':
                return True
    return False

def pos_player(arr):
    # player temporary coordinates
    x_player: int
    y_player: int

    for i in range(sizeA):
        for j in range(sizeA):
            if arr[i][j] == '@':
                x_player = i
                y_player = j

                return x_player, y_player

def check_new_pos_player(x_new, y_new, arr_check):
    x_temp, y_temp = pos_player(arr_check)  # function in order to receive current x, y coordinates of player

    if x_new > 9 or y_new > 9 or arr_check[x_new][y_new] == '*' or arr_check[x_new][y_new] == 'o':
        # move_num -= 1
        # ind_move_n += 1
        return True
    elif x_new != x_temp and y_new != y_temp:
        # move_num -= 1
        # ind_move_n += 1
        return True

    # fill track of player
    arr_check[x_temp][y_temp] = 'o'

    for i2 in range(x_temp, x_new, (1 if x_temp < x_new else -1)):
        arr_check[i2][y_new] = 'o'

    for j2 in range(y_temp, y_new, (1 if y_temp < y_new else -1)):
        arr_check[x_new][j2] = 'o'

def move_player(arr, move_num_cur):

    print("\nPlayer, move in orthogonal:")
    while move_num_cur:
        print("Remain steps: ", move_num_cur)

        y = abs(float(input("\t\tenter pos x -> ")))
        x = abs(float(input("\t\tenter pos y -> ")))
        print()
        x = int(x)
        y = int(y)
        x = (sizeA - 1) - x

        if check_new_pos_player(x, y, arr):  # function
            print("ERROR! pos x, y is not correct")
            move_num_cur -= 1
            clean_s()
            print_arr(arr)
            continue

        # check the position of enemy in order to kick it
        if arr[x][y] != '+':
            move_num_cur -= 1
        elif arr[x][y] == '+':
            move_num_cur -= 1
            move_num_cur += 5

        arr[x][y] = '@'

        if check_enemy(arr):
            clean_s()
            print()
            print_arr(arr)
            continue

        return move_num_cur
    else:
        return True

#======================MENU FUNCTION=============================#

def print_menu(ind_pos, arr, name_f = ""):
    for i in range(len(arr)):
        if i == ind_pos:
            print("-> \033[34m\033[43m{} {}\033[0m".format(name_f, arr[i]))
            continue
        print("   {} {}".format(name_f, arr[i]))

def receive_pos(ind_pos=0, name_f = ""):
    min_ind, max_ind = 0, 2
    if name_f == "set":
        max_ind = 4

    while True:
        direct = input(" ")

        # increment & decrement
        if not direct:
            return ind_pos, direct
        elif direct == 'W' or direct == 'w':
            ind_pos += 1
        elif direct == 'S' or direct == 's':
            ind_pos -= 1
        else:
            print("ERROR!")
            continue
            # return ind_pos

        # check position
        if ind_pos < min_ind:
            ind_pos = max_ind
        elif ind_pos > max_ind:
            ind_pos = min_ind

        return ind_pos, direct

def new_game(game_level = None):

    # dates
    enemy_num, ind_move, steps_qty = 0, 0, 0
    level = game_level
    level_lim = 5
    move_num = 5 * level

    arr_game = []
    fill_arr(arr_game)
    arr_game[1][1] = '@'

    print("\n\033[34m\033[43m New game\033[0m")

    while level < level_lim:

        print_data1()
        enemy_num = level

        fill_enemy(arr_game, level)
        print()
        print_arr(arr_game)
        print_data2(level, enemy_num)

        move_num = move_player(arr_game, move_num)
        if type(move_num) == bool and move_num:
            time.sleep(0)
            os.system('CLS')
            return "game_over"

        level += 1
        clean_s()

    else:
        clean_s()
        return "win"

def set_game(val = None):
    arr_set = [1, 2, 3, 4, 5]
    ind_set = 0

    while True:
        print("\n\033[34m\033[43m Settings\033[0m")
        print_menu(ind_set, arr_set, "Level")
        print(" \"w\" - Down, \"s\" - Up: -> ", end = '')
        ind_set, level_set = receive_pos(ind_set, "set")
        clean_s()

        if not level_set:
            ind_set += 1
            return ind_set

def exit_game(val = None):
    print("\n\033[34m\033[43m Exit\033[0m")
    return True

#======================main=============================#
sizeA: int = 10  # size of field game
arr_menu = ["New game", "Settings", "Exit"]
ind_menu = 0
value = 1
menu_f = {
    0: new_game,
    1: set_game,
    2: exit_game
}

while True:

    print("\nmenu:")
    print_menu(ind_menu, arr_menu)
    print(" \"w\" - Down, \"s\" - Up: ->", end='')
    ind_menu, operation = receive_pos(ind_menu)
    clean_s()

    if not operation:
        tempValue = menu_f[ind_menu](value)
        if type(tempValue) == int:
            value = tempValue
            continue
        elif type(tempValue) == str and tempValue == "game_over":
            print("\tGAME OVER!")
            continue
        elif type(tempValue) == str and tempValue == "win":
            print("\n\tYOU WIN! END of GAME")
            continue
        elif type(tempValue) == bool and tempValue:
            break
