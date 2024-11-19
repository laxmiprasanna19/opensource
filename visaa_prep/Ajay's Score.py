T = int(input())

for _ in range(T):
    X, N = map(int, input().split())

    points_per_test = X // 10

    score = points_per_test * N

    print(score)
