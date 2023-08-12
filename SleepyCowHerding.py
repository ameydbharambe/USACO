import sys

sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")
b, e, m = input().split()
b = int(b)
e = int(e)
m = int(m)
list1 = [b, e, m]
list1.sort()
minimum = 0
maximum = 0
difference = 100000000000
if list1[1] - list1[0] == 1 and list1[2] - list1[1] == 1:
    minimum = 0

elif list1[1] - list1[0] == 2 or list1[2] - list1[1] == 2:
    minimum = 1

else:
    minimum = 2 #?

print(minimum)
maximum = max(list1[2]- list1[1], list1[1]-list1[0]) # notice through test cases
print(maximum-1)



