# Kullanılacak yapılar

hamle = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# kazanma durumu ------------------

check_won1 = [
    [0, 0, 0, 1, 0, 2],
    [1, 0, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 2],  # yan yana

    [0, 0, 1, 0, 2, 0],  # alt alta
    [0, 1, 1, 1, 2, 1],
    [0, 2, 1, 2, 2, 2],

    [0, 0, 1, 1, 2, 2],  # capraz
]

sayac = 0

# Program başlangıcı ------------------
print("Welcome to the Tic-Tac-Toe Game!")

# Karakter seçimi ------------------
selected = False
player1 = ""
player2 = ""

while not selected:

    player1 = input("Player1, please choose your side (either X or O): ")

    if player1 == "X" or player1 == "O":
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
        selected = True

cikti = f"{hamle[0][0]}|{hamle[0][1]}|{hamle[0][2]}\n-+-+-\n{hamle[1][0]}|{hamle[1][1]}|{hamle[1][2]}\n-+-+-\n{hamle[2][0]}|{hamle[2][1]}|{hamle[2][2]}"

print(cikti)

# Oyun loop'u ------------------

while True:

    won = False
    turn = ["Player1", "Player2"]
    choice = input(f"{turn[sayac]}, please make your choice: ")

    a, b = choice.split(",")
    a = int(a)
    b = int(b)

    if hamle == 0:
        break

    if sayac == 0:
        if hamle[a][b] != " ":
            print(f"{hamle[a][b]} is already in the location {a},{b}. Skipping this turn.")

        else:
            hamle[a][b] = player1
            for i in check_won1:
                t1, t2, t3, t4, t5, t6 = i

                if hamle[t1][t2] == hamle[t3][t4] == hamle[t5][t6] and (
                        hamle[t1][t2] != " " or (hamle[t3][t4] != " ") or hamle[t5][t6] != " "):
                    won = True
                    break

    else:
        if hamle[a][b] != " ":
            print(f"{hamle[a][b]} is already in the location {a},{b}. Skipping this turn.")
        else:
            hamle[a][b] = player2

            for i in check_won1:
                t1, t2, t3, t4, t5, t6 = i

                if hamle[t1][t2] == hamle[t3][t4] == hamle[t5][t6] and (
                        hamle[t1][t2] != " " or (hamle[t3][t4] != " ") or hamle[t5][t6] != " "):
                    won = True
                    break
    cikti = f"{hamle[0][0]}|{hamle[0][1]}|{hamle[0][2]}\n-+-+-\n{hamle[1][0]}|{hamle[1][1]}|{hamle[1][2]}\n-+-+-\n{hamle[2][0]}|{hamle[2][1]}|{hamle[2][2]}"

    if won:
        print(cikti)
        print(turn[sayac], "has won the game!")
        break
    else:
        if sayac == 0:
            sayac = 1
        else:
            sayac = 0

    print(cikti)

    countForTie = 0
    for i in hamle:
        for j in i:
            if j != ' ':
                countForTie += 1

    if countForTie == 9:
        print("The game is finished! It is a tie.")
        break
