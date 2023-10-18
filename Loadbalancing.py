'''
N, B = input().split() #check tomorrow
N = int(N)
B = int(B)
sum1 = 0
sum2 = 0

minimumImbalance = N
list1 = []
relevantX = []
relevantY = []
for i in range(N):
    a, b = input().split()
    a = int(a)
    b = int(b)
    list1.append([a, b])
    if a+1 not in relevantX:
        relevantX.append(a+1)
    if b+1 not in relevantY: 
        relevantY.append(b+1)
    
for i in range(len(relevantX)):
    avg1 = relevantX[i]
    for j in range(len(relevantY)):
        avg2 = relevantY[j]
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for c in range(N):
            if list1[c][0] < avg1 and list1[c][1] < avg2:
                count1 += 1
            if list1[c][0] < avg1 and list1[c][1] > avg2:
                count2 += 1
            elif list1[c][0] > avg1 and list1[c][1] < avg2:
                count3 += 1
            elif list1[c][0] > avg1 and list1[c][1] > avg2:
                count4 += 1
            minimumImbalance = min(minimumImbalance, max(count1, count2, count3, count4))
print(minimumImbalance)'''
#with open("balancing.in") as read:
	# max_pos won't be used
cow_num, max_pos = input().split()
cow_num = int(cow_num)
max_pos = int(max_pos)

x_vals = []
y_vals = []
v_fence = set()
h_fence = set()
for _ in range(cow_num):
		x, y = input().split()
		x = int(x)
		y = int(y)
		x_vals.append(x)
		y_vals.append(y)
		v_fence.add(x_vals[-1] + 1)  # x-coords of relevant vertical fences
		h_fence.add(y_vals[-1] + 1)  # y-coords of relevant horizontal fences

# Loop through each pair of fences
min_imbalance = cow_num
for v in v_fence:
	for h in h_fence:
		top_left = 0
		top_right = 0
		bottom_left = 0
		bottom_right = 0

		# Count the number of cows in each region
		for c in range(cow_num):
			if x_vals[c] < v and y_vals[c] > h:
				top_left += 1
			elif x_vals[c] > v and y_vals[c] > h:
				top_right += 1
			if x_vals[c] < v and y_vals[c] < h:
				bottom_left += 1
			elif x_vals[c] > v and y_vals[c] < h:
				bottom_right += 1

		min_imbalance = min(
			min_imbalance, max(top_left, top_right, bottom_left, bottom_right)
		)

print(min_imbalance)
    
