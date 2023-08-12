N = int(input())
list1 = []
list2 = []
#read user inputs
for i in range(N):
    status, smallest, largest = input().split()
    smallest = int(smallest)
    largest = int(largest)
    list1.append([status, smallest, largest])
#algorithm to check before mile 1 values
for i in range(N):
    if list1[i][0] == 'none':
        list2.append(list1[i])
    if list1[i][0] == 'none' and list1[i+1][0] != 'none':
        break
index = list1.index(list2[0])
minimum = 1001
maximum = 1
for i in list2:
    minimum = min(minimum, i[1])
    maximum = max(maximum, i[2])
for j in range(index, -1, -1):
    if list1[
    
    
    
    