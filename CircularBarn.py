import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")
N = int(input())
list1 = []
for i in range(N):
    r = int(input())
    list1.append(r)
minDistance = 99999999999999999999999999 #set minimum distance as small as possible
for outsideDoor in range(N):
    currentDistance = 0
    for insideDoor in range(N):
        #(insideDoor+outsideDoor)%N calculates what the ideal index value would be in a circle (mod is cyclic) so index out of range is avoided
        currentDistance = currentDistance + insideDoor*list1[(insideDoor+outsideDoor)%N] #calculates currentDistance 
    minDistance = min(minDistance, currentDistance) #finds minimum distance
print(minDistance)
    