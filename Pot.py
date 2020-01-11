N = int(input())
X = 0
for i in range(0, N):
    P = input()
    X += int(P[0:(len(P) - 1)]) ** int(P[-1])
print(X)

