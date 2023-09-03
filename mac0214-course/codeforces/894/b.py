t = int(input())

while t > 0:

    n = int(input())

    b  = list(map(int, input().split()))

    a = [b[0]]
    m = 1

    for i in range(1, n):
        x = min(b[i], b[i-1])
        while x > b[i] or x >= b[i-1]:
            x -= 1
        
        if x >= 1:
            a.append(x)
            m += 1
        
        a.append(b[i])
        m += 1
    
    last = b[-1]
    if last > 1:
        a.append(last-1)
        m += 1

    print(m)
    numbers = ""
    for idx, number in enumerate(a):
        numbers += str(number)
        if idx == m-1:
            break
        else:
            numbers += " "

    print(numbers)

    t -= 1