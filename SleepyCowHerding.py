import sys
#To deal with Ad-Hoc Problems, first deal with easiest cases (e.g. in this case dif by 1) and go on to more complicated. Deal in small bits.
sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")
b, e, m = input().split()
b = int(b)
e = int(e)
m = int(m)
if e - b == m - e == 1: #this you can try using trial and error by considering simplest cases and moving to more complicated cases
    minimum = 0
elif e - b == 2 or m-e == 2:
    minimum = 1
else:
    minimum = 2
maximum = max(e-b, m-e)
print(minimum)
print(maximum-1) #we know this because we can move a corner number closer to one number and find the bigger gap and go one by one so it takes as long as possible to move in the middle



