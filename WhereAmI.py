'''N = int(input())
road = [*input()]
list1 = []
list2 = []
roadSet = set()
count = 0
for i in range(N):
    for j in range(N):
        if i+j < N:
            for k in range(j, i+j+1):
                list1.append(road[k])
            if list1 in roadSet:
                break
            else:
                roadSet.add(list1)
        list1.clear()
    if len(roadSet) == N - i:
        print(i)
        break
    else:
        roadSet.clear()'''

#correct solution
fin, fout = open('whereami.in'), open('whereami.out', 'w')
n = int(fin.readline().strip())
colors = fin.readline().strip()
ans = float('inf')

for i in range(len(colors)):
	seq = set()
	for j in range(n - i + 1):
		seq.add(colors[j:i+j]) #adds sequence of terms to set
	if len(seq) == (n - i + 1): #checks length so makes sure all terms are unique and is at maximum length
		ans = i #prints the smallest answer
		break

fout.write(str(ans)