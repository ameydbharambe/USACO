#can be more effective was lazy to make it effective

row1 = input()
row2 = input()
row3 = input()
row1List = [*row1]
row2List = [*row2]
row3List = [*row3]
c1 = row1List[0]
c2 = row1List[1]
c3 = row1List[2]
c4 = row2List[0]
c5 = row2List[1]
c6 = row2List[2]
c7 = row3List[0]
c8 = row3List[1]
c9 = row3List[2]
list1 = []
list2 = []
count1 = 0
count2 = 0
if c1 == c2 and c2 == c3 and c1 == c3:
    if list2.count([c1, c2, c3]) == 0:
        count1 += 1
        list2.append([c1, c2, c3])
list1.append(c1)
list1.append(c2)
list1.append(c3)
if list1.count(c1) == 2 or list1.count(c2) == 2:
    if list2.count([c1, c2, c3]) == 0:
        count2 += 1
        list2.append([c1, c2, c3])
list1.clear()
list1.append(c4)
list1.append(c5)
list1.append(c6)
if c4 == c5 and c5 == c6 and c4 == c6:
    if list2.count([c4, c5, c6]) == 0:
        count1 += 1
        list2.append([c4, c5, c6])
if list1.count(c4) == 2 or list1.count(c5) == 2:
    if list2.count([c4, c5, c6]) == 0:
        count2 += 1
        list2.append([c4, c5, c6])
list1.clear()
list1.append(c7)
list1.append(c8)
list1.append(c9)
if c7 == c8 and c8 == c9 and c7 == c9:
    if list2.count([c7, c8, c9]) == 0:
        count1 += 1
        list2.append([c7, c8, c9])
if list1.count(c7) == 2 or list1.count(c8) == 2:
    if list2.count([c7, c8, c9]) == 0:
        count2 += 1
        list2.append([c7, c8, c9])
list1.clear()
list1.append(c1)
list1.append(c4)
list1.append(c7)
if c1 == c4 and c4 == c7 and c1 == c7:
    if list2.count([c1, c4, c7]) == 0:
        count1 += 1
        list2.append([c1, c4, c7])
if list1.count(c1) == 2 or list1.count(c4) == 2:
    if list2.count([c1, c4, c7]) == 0:
        count2 += 1
        list2.append([c1, c4, c7])
list1.clear()
list1.append(c2)
list1.append(c5)
list1.append(c8)
if c2 == c5 and c2 == c8 and c5 == c8:
    if list2.count([c2, c5, c8]) == 0:
        count1 += 1
        list2.append([c2, c5, c8])
if list1.count(c2) == 2 or list1.count(c5) == 2:
    if list2.count([c2, c5, c8]) == 0:
        count2 += 1
        list2.append([c2, c5, c8])
list1.clear()
list1.append(c3)
list1.append(c6)
list1.append(c9)
if c3 == c6 and c3 == c9 and c6 == c9:
    if list2.count([c3, c6, c9]) == 0:
        count1 += 1
        list2.append([c3, c6, c9])
if list1.count(c3) == 2 or list1.count(c6) == 2:
    if list2.count([c3, c6, c9]) == 0:
        count2 += 1
        list2.append([c3, c6, c9])
list1.clear()
list1.append(c1)
list1.append(c5)
list1.append(c9)
if c1 == c5 and c5 == c9 and c1 == c9:
    if list2.count([c1, c5, c9]) == 0:
        count1 += 1
        list2.append([c1, c5, c9])
if list1.count(c1) == 2 or list1.count(c5) == 2:
    if list2.count([c1, c5, c9]) == 0:
        count2 += 1
        list2.append([c1, c5, c9])
list1.clear()
list1.append(c3)
list1.append(c5)
list1.append(c7)
if c3 == c5 and c5 == c7 and c3 == c7:
    if list2.count([c3, c5, c7]) == 0:
        count1 += 1
        list2.append([c3, c5, c7])
if list1.count(c3) == 2 or list1.count(c5) == 2:
    if list2.count([c3, c5, c7]) == 0:
        count2 += 1
        list2.append([c3, c5, c7])
list1.clear()
print(count1)
print(count2)

