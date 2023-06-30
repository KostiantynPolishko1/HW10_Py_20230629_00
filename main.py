#======================func=============================#

def print_menu(ind_pos = 0):
    print("\nmenu:")
    for i in range(len(arr_menu)):
        if i == ind_pos:
            print("->\t", arr_menu[i])
            continue
        print("\t", arr_menu[i])

def check_pos(ind_pos = 0):
    while True:
        direct = input("enter \"w\" / \"s\" -> ")

        # increment & decrement
        if direct == 'W' or direct == 'w':
            ind_pos += 1
        elif direct == 'S' or direct == 's':
            ind_pos -= 1
        else:
            print("ERROR!")
            continue

        # check position
        if ind_pos < 0:
            ind_pos = 2
        elif ind_pos > 2:
            ind_pos = 0

        return ind_pos

#======================main=============================#

arr_menu = ["New game", "Settings", "Exit"]
ind = 0

print("\n\"w\" - move Down\n\"s\" - move Up")

while True:
    print_menu(ind)
    ind = check_pos(ind)
