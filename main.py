import os
import time

#======================func=============================#

def print_menu(ind_pos = 0):
    print("\nmenu:")
    for i in range(len(arr_menu)):
        if i == ind_pos:
            print("-> ", arr_menu[i])
            continue
        print("   ", arr_menu[i])

def receive_pos(ind_pos = 0):
    while True:
        direct = input("   ")

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
        if ind_pos < 0:
            ind_pos = 2
        elif ind_pos > 2:
            ind_pos = 0

        return ind_pos, direct
def new_game():
    print("\n -> New game")

def set_game():
    print("\n -> Settings")

def exit_game():
    print("\n -> Exit")
    return True

#======================main=============================#

arr_menu = ["New game", "Settings", "Exit"]
ind = 0

menu_f = {
    0: new_game,
    1: set_game,
    2: exit_game
}
print("\n\"w\" - move Down\n\"s\" - move Up")

while True:
    print_menu(ind)
    ind, operation = receive_pos(ind)
    time.sleep(0)
    os.system('CLS')

    if not operation:
        logic = menu_f[ind]()
        if type(logic) == bool and logic:
            break
