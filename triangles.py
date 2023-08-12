import sys

sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")
N = int(input())
coords = []
area = 0
for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    coords.append([x, y])
coords.sort()
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            if (coords[a][0] == coords[b][0]) or (coords[a][0] == coords[c][0]) or (coords[b][0] == coords[c][0]):
                if (coords[a][1] == coords[b][1]) or (coords[a][1] == coords[c][1]) or (coords[b][1] == coords[c][1]):
                    part1 = (coords[a][0] * coords[b][1]) + (coords[b][0] * coords[c][1]) + (coords[c][0] * coords[a][1])
                    part2 = (coords[a][1] * coords[b][0]) + (coords[b][1] * coords[c][0]) + (coords[c][1] * coords[a][0])
                    area = max(area, abs(part1 - part2))
print(area)