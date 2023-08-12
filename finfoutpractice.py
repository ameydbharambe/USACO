import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, input().split())
c, d = map(int, input().split())

cover = [0] * 100
for i in range(a, b):
	cover[i] = 1
for i in range(c, d):
	cover[i] = 1

ans = 0
for i in range(len(cover)):
	ans += cover[i]
print(ans)