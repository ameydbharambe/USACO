#key idea here is to find the differences and see which one is the biggest
import sys

sys.stdin = open("mowing.in", "r")
sys.stdout = open("mowing.out", "w")
N = int(input())
list1 = []
list2 = []
list3 = []
x = 9999999999
xCoord = 0
yCoord = 0
for i in range(N):
    D, S = input().split()
    S = int(S)
    list1.append([D, S])
for i in list1:
    for j in range(1, i[1]+1):
        if i[0] == 'N':
            yCoord += 1
            list2.append([xCoord, yCoord])
        if i[0] == 'S':
            yCoord -= 1
            list2.append([xCoord, yCoord])
        if i[0] == 'W':
            xCoord -= 1
            list2.append([xCoord, yCoord])
        if i[0] == 'E':
            xCoord += 1
            list2.append([xCoord, yCoord])
for i in list2:
    if list2.count(i) > 1:
        diff = 10**20
        list3 = [k+1 for k in range(len(list2)) if list2[k] == i]
        for a in range(len(list3)-1):
            for b in range(a+1, len(list3)):
                diff = min(diff, abs(list3[a]-list3[b]))
        x = min(x, diff)
        list3.clear()
if x == 9999999999:
    print(-1)
else:
    print(x)