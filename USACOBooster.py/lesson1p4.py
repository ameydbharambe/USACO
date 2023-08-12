String = input()
StringList = list(String)
list1 = []
count = 0
count1 = 0
index = 2
index1 = 0
for j in range(5):
    list1.append([])
    for i in range(4*len(String)+1):
        list1[j].append('.')
for a in range(5):
    if a == 0 or a == 4:
        while index < len(list1[a]):
            list1[a][index] = '#'
            if list1[a][index] == '#':
                count = count + 1
            if count%3 == 0:
                list1[a][index] = '*'
            index = index + 4
    elif a == 1 or a == 3:
        for k in range(len(list1[0])):
            if list1[0][k] == '#':
                list1[a][k-1] = '#'
                list1[a][k+1] = '#'
            elif list1[0][k] == '*':
                list1[a][k-1] = '*'
                list1[a][k+1] = '*'
    else:
        while index1 < len(list1[2]):
            list1[a][index1] = '#'
            if list1[a][index1] == '#':
                count1 = count1 + 1
            if count1%3 == 0 or (count1 != 1 and count1%3 == 1):
                list1[a][index1] = '*'
            index1 = index1 + 4
        for z in StringList:
            for y in range(len(list1[0])):
                if list1[0][y] == '#' or list1[0][y] == '*':
                    list1[a][y] = z
for k in range(5):
    print(list1[k])