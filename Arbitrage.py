liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

mp = {}
flag = 0
def dfs(ans, cur, depth, v):
    global flag
    if depth == 5 or flag == 1:
        return
    v.append(cur)
    if cur == 2:
        if ans > 20:
            flag = 1
            # print(cur)
            # print(ans)
            # print("ok")
            print("path: ", end = '')
            v.pop()
            for i in v:
                if(i == 1):
                    print("tokenA->", end = '')
                elif(i == 2):
                    print("tokenB->", end = '')
                elif(i == 3):
                    print("tokenC->", end = '')
                elif(i == 4):
                    print("tokenD->", end = '')
                elif(i == 5):
                    print("tokenE->", end = '')
            print("tokenB, tokenB balance=", end = '')
            print(ret)
            return
    else:
        x, y = mp[(cur, 2)]
        ret = 997 * ans * y / (1000 * x + 997 * ans)
        if ret > 20:
            flag = 1
            v.append(2)
            # print(cur)
            # print(ret)
            # print("ok")
            print("path: ", end = '')
            v.pop()
            for i in v:
                if(i == 1):
                    print("tokenA->", end = '')
                elif(i == 2):
                    print("tokenB->", end = '')
                elif(i == 3):
                    print("tokenC->", end = '')
                elif(i == 4):
                    print("tokenD->", end = '')
                elif(i == 5):
                    print("tokenE->", end = '')
            print("tokenB, tokenB balance=", end = '')
            print(ret)
            return

    for i in range(1, 6):
        if i == cur:
            continue
        x, y = mp[(cur, i)]
        ret = 997 * ans * y / (1000 * x + 997 * ans)
        dfs(ret, i, depth + 1, list(v))

if __name__ == "__main__":
    mp[(1, 2)] = (17, 10)
    mp[(1, 3)] = (11, 7)
    mp[(1, 4)] = (15, 9)
    mp[(1, 5)] = (21, 5)
    mp[(2, 3)] = (36, 4)
    mp[(2, 4)] = (13, 6)
    mp[(2, 5)] = (25, 3)
    mp[(3, 4)] = (30, 12)
    mp[(3, 5)] = (10, 8)
    mp[(4, 5)] = (60, 25)

    mp[(2, 1)] = (10, 17)
    mp[(3, 1)] = (7, 11)
    mp[(4, 1)] = (9, 15)
    mp[(5, 1)] = (5, 21)
    mp[(3, 2)] = (4, 36)
    mp[(4, 2)] = (6, 13)
    mp[(5, 2)] = (3, 25)
    mp[(4, 3)] = (12, 30)
    mp[(5, 3)] = (8, 10)
    mp[(5, 4)] = (25, 60)

    v = []

    dfs(5, 2, 0, v)

