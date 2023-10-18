#STEPS TO SOLVE:
#1. CHECK IF SUM IS PRIME, IF YES, THEN CHECK IF EVERY TERMS IS SAME OR SOME O'S THEN ADD NUMBER OF ZEROES FOR OPERATION
#2. IF NOT PRIME, THEN FIND ALL FACTORS AND COUNT TILL REACH EACH FACTOR, IF NOT POSSIBLE THEN DON'T COUNT
'''import math
def Prime(integer):
    for i in range(2, int(math.sqrt(integer)) + 1):
        if integer%i == 0:
            return False
            break
    return True

T = int(input())
factors = []
postElsie = []
list1 = []
for i in range(T):
    count = 0
    N = int(input())
    log = input().split()
    for i in range(len(log)):
        log[i] = int(log[i])
    if log == [log[0]]*N:
        print(0)
    if Prime(N) == True:
        count = len(log)
        print(count)
                
    elif Prime(N) == False:
        for j in range(2, N//2 + 1):
            if N%j == 0:
                factors.append(j)
        for k in factors:
            factor = k
            wanted = N//factor
            sum = 0
            for n in range(len(log)):
                count += 1
                if sum != wanted:
                    sum += log[n]
                elif sum == wanted:
                    postElsie.append(sum)
                    sum = 0
                    sum += log[n]
            if postElsie.count(wanted) == len(postElsie):
                list1.append(count//2)
            postElsie.clear()
        list1.sort()
        print(list1[0])
        factors.clear()
        list1.clear()'''
for _ in range(int(input())):
    n = int(input())
    elsie_log = [int(i) for i in input().split()]
    assert len(elsie_log) == n

    log_sum = sum(elsie_log)

	# Try all possible number of hours after modification
    for num_hours in range(log_sum + 1):
		# The sum must be divisible by num_hours
    if num_hours != 0 and log_sum % num_hours != 0: #check if hours is factor and not 0 otherwise will not work 
			continue

		# Updates the program with number of hours being used
		curr_sum = 0  # The current number of hours Elsie's logging
		for h in elsie_log:
			curr_sum += h #similar to my logic where I counted the groups of the factor by adding the terms
			if curr_sum > num_hours:
				break  # curr_sum can't exceed num_hours
			elif curr_sum == num_hours:
				curr_sum = 0
		else: #else case is held for exceptions such as num_hours only working is 0
			if num_hours == 0:
				# Handle the edge case where num_hours is 0
				print(0)
			else:
				# sum/num_hours is the total # of classes AFTER modifying
				print(n - log_sum // num_hours)
			break
                
                    