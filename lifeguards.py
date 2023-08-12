import sys

sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")
N = int(input())
list1 = []
list2 = []
length = 0
count = 0
for i in range(N):
    start, end = input().split()
    start = int(start)
    end = int(end)
    list1.append([start, end])
for set in range(N):
    for rest in range(N):
        if rest != set:
            for j in range(list1[rest][0], list1[rest][1]): #instead of counting intervals deal with each time and check how many times its counted (end time not included)
                if j not in list2:
                    list2.append(j)
    length = max(length, len(list2))
    list2.clear()
print(length)