for i in range(int(input())):
    X, Y = map(int, input().split())
    if Y < X:
        print(X - Y)