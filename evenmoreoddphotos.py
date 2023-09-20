N = int(input())
breedID = input().split()
count = 0
breed = []
sum = True #True is even, False is odd
while len(breedID) > 0:
    if sum == True:
        sum1 = int(breedID[0])
        breed.append(breedID[0])
        i = 1
        while sum1%2 != 0:
            sum1 += int(breedID[i])
            breed.append(breedID[i])
            i += 1
        for i in breed:
            breedID.remove(i)
        breed.clear()
        count += 1
        sum = False
    elif sum == False:
        sum1 = int(breedID[0])
        breed.append(breedID[0])
        i = 1
        while sum1%2 == 0:
            sum1 += int(breedID[i])
            breed.append(breedID[i])
            i += 1
        for i in breed:
            breedID.remove(i)
        breed.clear()
        count += 1
        sum = True
print(count)
            
        
        
    
    