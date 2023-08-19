t = int(input())
out = []
while t > 0:
    n = int(input())

    cuts = 0

    for i in range(n):
        a, b = map(int, input().split())
        if b < a:
            cuts += 1

    print(cuts)

    t -= 1
