import sys

sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")
N = int(input())
cows = [7]*3
count = 0
log = []
best = []
for i in range(N):
    day, cow, change = input().split()
    day = int(day)
    log.append([day, cow, change])
log.sort()
for j in range(N):
    best1 = []
    parity = [*log[j][2]]
    #code that changes value for each cow
    if log[j][1] == "Bessie":
        if parity[0] == "+":
            cows[0] += int(parity[1])
        else:
            cows[0] -= int(parity[1])
    elif log[j][1] == "Elsie":
        if parity[0] == "+":
            cows[1] += int(parity[1])
        else:
            cows[1] -= int(parity[1])
    else:
        if parity[0] == "+":
            cows[2] += int(parity[1])
        else:
            cows[2] -= int(parity[1])
    #code that compares if there was any change in #1 cow
    if cows[0] == max(cows):
        best1.append("Bessie")
    if cows[1] == max(cows):
        best1.append("Elsie")
    if cows[2] == max(cows):
        best1.append("Mildred")
    if best1 != best:
        count += 1
        best.clear()
        for i in range(len(best1)):
            best.append(best1[i])
    best1.clear()
print(count)
        
        
            
    
