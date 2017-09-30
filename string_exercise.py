#1
word1 = 'bananas'
count1 = 0
for letter in word1:
    if letter == 'a':
        count1 = count1 + 1
    if letter == 'b':
        count1 = count1 + 2
    if letter == 'n':
        count1 = count1 + 14
    if letter == 's': 
        count1 = count1 + 19
counta = '$'+str(count1)
print('bananas', counta)

word2 = 'rice'
count2 = 0
for letter in word2:
    if letter == 'c':
        count2 = count2 + 3
    if letter == 'e':
        count2 = count2 + 5
    if letter == 'i':
        count2 = count2 + 9
    if letter == 'r':
        count2 = count2 + 18
countb = '$'+str(count2)
print('rice', countb)

word3 = 'paprika'
count3 = 0
for letter in word3:
    if letter == 'a':
        count3 = count3 + 1
    if letter == 'i':
        count3 = count3 + 9
    if letter == 'k':
        count3 = count3 + 11
    if letter == 'p':
        count3 = count3 + 16
    if letter == 'r':
        count3 = count3 + 18
countc = '$'+str(count3)
print('parika', countc)

word4 = 'potato chips'
count4 = 0
for letter in word4:
    if letter == 'a':
        count4 = count4 + 1
    if letter == 'i':
        count4 = count4 + 9
    if letter == 'h':
        count4 = count4 + 8
    if letter == 'o':
        count4 = count4 + 15
    if letter == 'p':
        count4 = count4 + 16
    if letter == 's':
        count4 = count4 + 19
    if letter == 't':
        count4 = count4 + 20 
countd = '$'+str(count4)
print('potato chips', countd)
print('----------------------------')
total = count1 + count2 + count3 + count4
count_total = '$'+str(total)
print('Total', count_total)


#2

print('bananas', '%10.2f'%count1)
print('rice', '%13.2f'%count2)
print('paprika', '%10.2f'%count3)
print('potato chips', '%5.2f'%count4)
print('----------------------------')
print('Total', '%13.2f'%total)

#3

print('bananas', '%10.2f'%count1)
print('rice', '%13.2f'%count2)
print('paprika', '%10.2f'%count3)
print('----------------------------')
print('Total', '%13.2f'%total)

