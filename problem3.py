
N = int(input())
list1 = input().split()
list2 = []
for i in range(N):
    list1[i] = int(list1[i])
length = len(list1)
starting = 2
while starting <= N:
    for i in range(0, N - starting):
        for j in range(i, i+starting+1):
            list2.append(list1[j])
        total = sum(list2)
        average = total/starting
        if average.is_integer():
            average = int(average)
            if average in list1:
                length = length + 1
        list2.clear()
    starting = starting + 1
print(length)
            


        

