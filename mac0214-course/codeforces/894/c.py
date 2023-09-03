def binarySearch(arr, x):
    # encontrar o indice do menor elemento que é >= x
    l = 0
    r = len(arr)-1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= x:
            l = mid + 1
        else:
            r = mid
    return l - 1
    
t = int(input())

while t > 0:

    n = int(input())

    hs = list(map(int, input().split()))

    if n != hs[0]:
        print("NO")
        t -= 1
        continue

    new_hs = []

    for i in range(1, hs[0]+1):
        cnt = 0
        # for h in hs:
        #     if h >= i:
        #         cnt += 1
        idx = binarySearch(hs, i)

        new_hs.append(idx+1)
        
    symm = True

    print(new_hs)

    if len(hs) == len(new_hs):
        for idx, h in enumerate(hs):
            if h != new_hs[idx]:
                symm = False
                break
    else:
        symm = False

    if symm:
        print("YES")
    else:
        print("NO")

    t -= 1