import sys

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")
N, K = input().split()
N = int(N)
K = int(K)
list2 = []
count = 0
for i in range(N):
    list1 = [int(x) for x in input().split(" ")]
    list2.append(list1)
for b in range(K-1):
    for c in range(b+1, K):
        term1 = list2[0][b]
        term2 = list2[0][c]
        count1 = 0
        for a in range(N):
            if list2[a].index(term1) < list2[a].index(term2):
                count1 += 1
        if count1 == N:
            count += 1
print(count)