N = int(input().strip())
string1 = input().strip()
Evalues = list(map(int, input().strip().split()))
count = 0

for j in range(N):
    for k in range(j, Evalues[j]):
        if string1[k] == 'G':
            if k == j:
                if string1[:Evalues[j]].count('G') == string1.count('G'):
                    count += 1
            else:
                if string1[j:Evalues[j]].count('G') == string1.count('G'):
                    count += 1
        elif string1[k] == 'H':
            if k == j:
                if string1[:Evalues[j]].count('H') == string1.count('H'):
                    count += 1
            else:
                if string1[j:Evalues[j]].count('H') == string1.count('H'):
                    count += 1

print(count)



