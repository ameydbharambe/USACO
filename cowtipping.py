import sys

sys.stdin = open("cowtip.in", "r")
sys.stdout = open("cowtip.out", "w")
N = int(input())
list1 = [] #I literally cannot think any name for the matrix
count = 0
for i in range(N):
    sequence = input()
    sequenceList = list(sequence)
    list1.append(sequenceList)
while list1 != [["0"]*N]*N:
    for length in range(N-1, -1, -1):#essentially find the most farthest 1 so the rectangle is made large as possible so a larger area is covered
        for width in range(N-1, -1, -1):
            if list1[length][width] == "1":
                for rectL in range(0, length+1):
                    for rectW in range(0, width+1):
                        if list1[rectL][rectW] == "0":
                            list1[rectL][rectW] = "1"
                        else:
                            list1[rectL][rectW] = "0"
                count += 1
print(count)
                
            