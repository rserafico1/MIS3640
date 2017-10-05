#Exercise 1
fin = open('words.txt')
line = fin.readline()
print(line)

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)

def find_long_words():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))

find_long_words()

def has_no_e(word):
    for letter in word: 
        if letter.lower() == 'e':
            return False
        return True

    return not 'e' in word.lower()

print(has_no_e('Babson'))
print(has_no_e('College'))

def find_words_no_e():
    fin = open('words.txt')
    counter_no_e = 0
    counter_total = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if has_no_e(word):
            #print(word)
            counter_no_e += 1
    return counter_no_e/counter_total

#find_words_no_e()
print('The percentage of the words with no "e" is {:.2f}%.'.format(find_words_no_e()*100))

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
        else:
            return True

print(avoids('Babson', 'ab'))
print(avoids('College','ab'))


def find_words_no_vowels():
    fin = open('words.txt')
    counter_no_vowels = 0
    counter_total = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if avoids(word, 'aeiou'):
            counter_no_vowels += 1
        return counter_no_vowels/counter_total

print('The percentage of the words with vowels is {:.4f}%.'.format(find_words_no_vowels()*100))

def uses_only(word, available):
    for letter in word: 
        if letter not in available:
            return False
    return True

print(uses_only(apple, asdfg))

def uses_all(word, required):
    for letter in required: 
        if letter not in word:
            return False
    return True

print(uses_all(book, e))

def uses_all(word, required):
    return uses_only(required, word)

print(uses_all(road, o))

#Exercise 2

#recursion
def is_abecedarian(word):
    previous = c
    if word == 0:
        return False
    else:
        return True
print(is_abecedarian(arm))

#loop
def is_abecedarian(word):
    c = 0
    previous = word[0]
    for c in word:
        while (c < previous):
            print('We will compare:', word)
            c = c +1     

print(is_abecedarian(pop))