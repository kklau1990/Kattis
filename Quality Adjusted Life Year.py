QALY = 0
N = int(input())
for i in range(0, N):
    q, y = map(float, input().split())
    QALY += q*y

print(QALY)