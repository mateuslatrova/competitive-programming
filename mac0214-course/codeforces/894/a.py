t = int(input())

while (t > 0):
    n, m = map(int, input().split())

    carpet = []

    for i in range(n):
        line = list(input())
        carpet.append(line)

    vika = "vika"

    # mapear, para cada letra, em quais colunas ocorre.
    # depois, verificar se é possível...

    l_to_c = {l: set() for l in vika}
    # Coluna a coluna da esquerda para a direita
    for j in range(m):
        for i in range(n):
            l = carpet[i][j]
            if l in vika:
                l_to_c[l].add(j)

    prev_pos = -1
    curr_pos = 0

    likes = True

    for idx, l in enumerate(vika):
        
        if not likes:
            break

        positions = sorted(list(l_to_c[l]))

        if not l_to_c[l]:
            likes = False
            break

        found_pos = False
        for pos in positions:
            if pos > prev_pos:
                curr_pos = pos
                found_pos = True
                break

        if not found_pos:
            likes = False
            break
        
        prev_pos = curr_pos

    if likes:
        print("YES")
    else:
        print("NO")

    t -= 1

