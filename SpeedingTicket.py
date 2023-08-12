import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")
N, M = input().split()
N = int(N)
M = int(M)
initial = 0
initial2 = 0
difference = 0
list1 = []
list2 = []
for i in range(N):
    r1, s1 = input().split()
    r1 = int(r1)
    s1 = int(s1)
    for j in range(initial, r1+initial):
        list1.append([j, s1])
    initial = initial + r1 + 1
for i in range(M):
    r2, s2 = input().split()
    r2 = int(r2)
    s2 = int(s2)
    for j in range(initial2, r2+initial2):
        list2.append([j, s2])
    initial2 = initial2 + r2 + 1
for i in range(100):
    subdifference = list2[i][1] - list1[i][1]
    difference = max(subdifference, difference)
print(difference)


        
    
    
        
    
    
    