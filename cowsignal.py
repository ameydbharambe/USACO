import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")
M, N, K = input().split()
M = int(M)
N = int(N)
K = int(K)
finalSignal = []
for i in range(M):
    signal = input()
    signalArray = [char for char in signal]
    finalSignal.append(signalArray)
for i in range(M):
    newList = []
    for j in range(N):
        for k in range(K):
            newList.append(finalSignal[i][j])
    for n in range(K):
        print("".join(newList))
