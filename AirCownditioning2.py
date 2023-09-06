numOfCows, numOfHVACS = input().split()
numOfCows, numOfHVACS = int(numOfCows), int(numOfHVACS)
coolingNeeds = [0 for i in range(100)]
for i in range(numOfCows):
    tempCow = input().split()
    for r in range(int(tempCow[0])-1, int(tempCow[1])):
        coolingNeeds[r] = int(tempCow[2])
airCons = [[int(i) for i in input().split()] for r in range(numOfHVACS)]
bestCase = 1000000000

for i in range(1 << numOfHVACS):
    tempCoolingNeeds = coolingNeeds[:]
    moneyCounter = 0
    for r in range(numOfHVACS):
        if (1 << r) & i:
            for s in range(airCons[r][0] - 1, airCons[r][1]):
                tempCoolingNeeds[s] -= airCons[r][2]
            moneyCounter += airCons[r][3]
    if max(tempCoolingNeeds) <= 0:
        bestCase = min(bestCase, moneyCounter)

print(bestCase)