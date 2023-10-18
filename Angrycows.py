import sys

sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")
N = int(input())
listOfX = []
alternate = []
for i in range(N):
    x = int(input())
    listOfX.append(x)
    alternate.append(x)
listOfX.sort()
alternate.sort()
countFinal = 0
for i in range(N):
    launch = alternate[i]
    launch1 = alternate[i]
    launch2 = alternate[i]
    count = 1
    count1 = 0
    while launch1 in listOfX and launch2 in listOfX:
        launch3 = launch1
        launch1 = launch1 - count #consider the fact that what if this is not a crate value
        launch4 = launch2
        launch2 = launch2 + count
        for j in range(N):
            if listOfX[j] >= launch1 and listOfX[j] <= launch3:
                count1+= 1
            elif launch4 <= listOfX[j] and listOfX[j] <= launch2:
                count1 += 1
        count += 1
    countFinal = max(count1, countFinal)
    
print(countFinal-2)
    
        


    