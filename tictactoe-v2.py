sira = ["Player1", "Player2"]
marked = 0

def choose_side() -> tuple:

    p1 = input("Player1, please choose your side (either X or O): ")

    if p1 == "X":
        p2 = "O"
        return p1, p2
    elif p1 == "O":
        p2 = "X"
        return p1, p2
    else:
        return choose_side()


def display_enviroment(board) -> None:
    print(board)


# Kısım dolu mu ?
def implychoices(t, row, column) -> bool:
    if t[row][column] == " ":
        return True
    return False


# Seçim
def makechoice(sayac) -> tuple:
    a = input(f"{sira[0 if sayac % 2 == 0 else 1]}, please make your choice: ")
    row, column = a.split(",")
    row = int(row)
    column = int(column)
    return row, column


# Yerler doldu mu
def checkboard(marked) -> bool:
    if marked == 9:
        return True

    return False


# Kazanma durumu
def iswinner(t) -> bool:
    if t[0][0] == t[0][1] == t[0][2] != " ":
        return True

    elif t[1][0] == t[1][1] == t[1][2] != " ":
        return True

    elif t[2][0] == t[2][1] == t[2][2] != " ":
        return True

    elif t[0][0] == t[1][0] == t[2][0] != " ":
        return True

    elif t[0][1] == t[1][1] == t[2][1] != " ":
        return True

    elif t[0][2] == t[1][2] == t[2][2] != " ":
        return True

    elif t[0][0] == t[1][1] == t[2][2] != " ":
        return True


sayac = 0

print("Welcome to the Tic-Tac-Toe Game!")

player1, player2 = choose_side()
t = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while not iswinner(t):
    board = f"{t[0][0]}|{t[0][1]}|{t[0][2]}\n-+-+-\n{t[1][0]}|{t[1][1]}|{t[1][2]}\n-+-+-\n{t[2][0]}|{t[2][1]}|{t[2][2]}"

    if checkboard(marked):
        display_enviroment(board)
        print("The game is finished! It is a tie.")
        break
    display_enviroment(board)
    a, b = makechoice(sayac)
    if implychoices(t, a, b):
        t[a][b] = player1 if sayac % 2 == 0 else player2

    else:
        print(f"{t[a][b]} is already in the location {a},{b}. Skipping this turn.")

    if not iswinner(t):
        sayac += 1
        marked += 1


board = f"{t[0][0]}|{t[0][1]}|{t[0][2]}\n-+-+-\n{t[1][0]}|{t[1][1]}|{t[1][2]}\n-+-+-\n{t[2][0]}|{t[2][1]}|{t[2][2]}"
if iswinner(t):
    if sayac % 2 == 0:
        display_enviroment(board)
        print("Player1 has won the game!")

    else:
        display_enviroment(board)
        print("Player2 has won the game!")

