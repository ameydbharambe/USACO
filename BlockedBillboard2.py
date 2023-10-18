
x1, y1, x2, y2 = input().split()#main logic is just case work for all possibilities
x3, y3, x4, y4 = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x3 = int(x3)
y3 = int(y3)
x4 = int(x4)
y4 = int(y4)
Rect1 = []
Rect2 = []
area = 1000000000
for i in range(x1, x2+1): #find lattice points in lawn mower
    for j in range(y1, y2+1):
        Rect1.append([i, j])
for a in range(x3, x4+1): #find lattice points in cow feed
    for b in range(y3, y4+1):
        Rect2.append([a, b])
result = [n for n in Rect1 if n in Rect2] #Finds mutual lattice points
if len(result) == 0:
    print(abs(x2-x1) * abs(y2 - y1))
elif result == Rect1:
    print(0)
elif [x2, y2] in result:
    for i in range(len(result)-1, -1, -1):
        if result[i][1] == y1 and (abs(x2 - result[i][0]) * abs(y2 - y1) != 0):
            print(abs(x2 - result[i][0]) * abs(y2 - y1))
            break
            
elif [x1, y1] in result:
    for i in range(len(result)):
        if result[i][1] == y1 and (abs(x2 - result[i][0]) * abs(y2 - y1) != 0):
            print(abs(x2 - result[i][0]) * abs(y2 - y1))
            break
        
else:
    print(abs(x2-x1) * abs(y2 - y1))        
            



        