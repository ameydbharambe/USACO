import sys
from collections import Counter
sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")
N = int(input())
cowsMilk = [0, 0, 0, 0, 0, 0, 0]
for i in range(N):
    cow, milk = input().split()
    milk = int(milk)
    if cow == "Bessie":
        cowsMilk[0] += milk
    elif cow == "Elsie":
        cowsMilk[1] += milk
    elif cow == "Daisy":
        cowsMilk[2] += milk
    elif cow == "Gertie":
        cowsMilk[3] += milk
    elif cow == "Annabelle":
        cowsMilk[4] += milk
    elif cow == "Maggie":
        cowsMilk[5] += milk
    else:
        cowsMilk[6] += milk
cowsDic = {"Bessie" : cowsMilk[0], "Elsie" : cowsMilk[1], "Daisy" : cowsMilk[2], "Gertie" : cowsMilk[3], "Annabelle" : cowsMilk[4], "Maggie" : cowsMilk[5], "Henrietta" : cowsMilk[6]}
cowsMilk.sort()
minimum = min(cowsMilk)

for i in range(7):
    if cowsMilk[i] != minimum:
        wanted = cowsMilk[i]
        break
if cowsMilk[0] == cowsMilk[1] == cowsMilk[2] == cowsMilk[3] == cowsMilk[4] == cowsMilk[5] == cowsMilk[6]:
    wanted = minimum
wantedCounts = Counter(cowsDic.values())
if wantedCounts[wanted] == 1:
    value = next(iter({n for n in cowsDic if cowsDic[n] == wanted}))
else:
    value = "Tie"
print(value)



    
    