import math
N = int(input())
count = math.inf #set minimum value as large as possible
list1 = []
list2 = []
for i in range(N):
    direction, p = input().split()
    p = int(p)
    list1.append([direction, p])
for i in range(N):
    liars = 0
    for j in range(N):
        if (list1[j][0] == "G") and (list1[j][1] > list1[i][1]):#check if consistent with other data
            liars += 1
        elif (list1[j][0] == "L") and (list1[j][1] < list1[i][1]): #check if consistent with other data
            liars += 1
    count = min(liars, count) #make count as small as possible after checking each cow
print(count)


