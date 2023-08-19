t = int(input())

for i in range(t):
    n = int(input())
    k = 2
    valid = False

    # 15 e 255
    while True:
        soma = 1 + k + k**2
        if n < soma:
            valid = False
            break

        i = 3
        while n > soma:
            soma += k**i
            i += 1

        if n == soma:
            valid = True
            break

        k += 1

    if valid:
        print("YES")
    else:
        print("NO")
