import sys

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")
cows = input()
cowsList = [*cows]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count1 = 0 
for i in range(26):
    letter = alphabet[i]
    start = cowsList.index(letter)
    end = 51 - cowsList[::-1].index(letter)
    for a in range(start+1, end):
        wanted = cowsList[a]
        for b in range(end+1, 52):
            if cowsList[b] == wanted:
                count1 += 1
                break
print(count1)
        