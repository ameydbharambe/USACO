import sys

sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
N, K = input().split()
N = int(N)
K = int(K)
list1 = []
for i in range(N):
    diamond = int(input())
    list1.append(diamond)
answer = 0
for i in range(N):
    test = 0 #test maximum
    for j in range(N):
        if list1[j] >=list1[i] and list1[j] <= list1[i] + K: #check if each term is fits the difference of K range
            test = test + 1 #add to total
    if test > answer: #maximize total
        answer = test
print(answer)