import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")
X, Y, M = input().split()
X = int(X)
Y = int(Y)
M = int(M)
maximum = 0
for x in range(M//X + 1):
    for y in range(M//Y + 1):
        if X*x + Y*y <= M:
            maximum = max(X*x + Y*y, maximum)
print(maximum)
            


        
    








