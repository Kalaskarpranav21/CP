def cbin(n, k):
    if k > n // 2:
        k = n - k
    top = 1
    bot = 1
    for i in range(2, k + 1):
        bot *= i
    for i in range(n - k + 1, n + 1):
        top *= i
    return top // bot

def rec(t, b):
    res = 1
    if b > 1:
        dif = t // b
        if dif == 1:
            for i in range(2, b + 1):
                res *= i
        else:
            for _ in range(b - 1):
                res *= cbin(t, dif)
            t -= dif
            res *= rec(dif - 1, b) ** b
    return res

while True:
    try:
        b, l = map(int, input().split())
        if b == 0 and l == 0:  # Check for termination condition
            break
        print(rec(l, b))  # Call the recursive function and print the result
    except EOFError:  # Catch EOFError to handle end of input
        break
