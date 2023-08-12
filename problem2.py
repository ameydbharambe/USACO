T = int(input())
while T > 0:
    N, K  = input().split()
    N = int(N)
    K = int(K)
    sequence = input()
    sequenceList = list(sequence)
    efficient = []
    for i in range(N):
        efficient.append('.')
    lastFoodG = -K-1
    lastFoodH = -K-1
    count = 0
    for i in range(N):
        if sequenceList[i] == 'G' and (i - lastFoodG) > K:
            lastFoodG = min(i+K, N-1)
            if efficient[lastFoodG] != '.':
                lastFoodG = lastFoodG - 1
            efficient[lastFoodG] = 'G'
            count = count + 1
        elif (sequenceList[i] == 'H') and (i - lastFoodH) > K:
            lastFoodH = min(i+K, N-1)
            if efficient[lastFoodH] != '.':
                lastFoodH = lastFoodH - 1
            efficient[lastFoodH] = 'H'
            count = count + 1
    T = T - 1
    print(count)
    print(''.join(efficient))