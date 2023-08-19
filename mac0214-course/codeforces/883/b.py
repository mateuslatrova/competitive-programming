t = int(input())

for i in range(t):
    game = []

    for i in range(3):
        line = input()
        game.append(list(line))

    # Horizontal
    won = True

    for i in range(3):
        first = game[i][0]
        if first == ".":
            won = False
            continue

        won = True
        for j in range(1, 3):
            if game[i][j] != first:
                won = False
                break
        if won:
            print(first)
            break

    if won:
        continue

    # ####  vertical
    won = True

    for j in range(3):
        first = game[0][j]
        if first == ".":
            won = False
            continue

        won = True
        for i in range(1, 3):
            if game[i][j] != first:
                won = False
                break
        if won:
            print(first)
            break

    if won:
        continue

    # diagonal principal
    won = True

    first = game[0][0]
    if first != ".":
        for i in range(3):
            if game[i][i] != first:
                won = False
                break
    else:
        won = False

    if won:
        print(first)
        continue

    # diagonal secundaria
    won = True

    first = game[0][2]
    if first != ".":
        for i, j in [(0, 2), (1, 1), (2, 0)]:
            if game[i][j] != first:
                won = False
                break
    else:
        won = False

    if won:
        print(first)
    else:
        print("DRAW")
