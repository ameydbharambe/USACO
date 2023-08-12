import string
import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")
N = int(input())
list1 = []
for i in range(N):
    word1, word2 = input().split()
    list1.append([*word1])
    list1.append([*word2])
for j in list(string.ascii_lowercase):
    count = 0
    for k in range(0, 2*N, 2):
        count1 = 0
        count2 = 0
        for l in range(0, len(list1[k])):
            if list1[k][l] == j:
                count1 = count1 + 1
        for l in range(0, len(list1[k+1])):
            if list1[k+1][l] == j:
                count2 = count2 + 1
        count = count + max(count1, count2)
    print(count)
                
    