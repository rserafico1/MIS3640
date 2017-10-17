def nested_sum(t):
    total = 0  
    for i in t:
        if isinstance(i, list): 
            total += nested_sum(i)
        else:
            total += i
    return total

t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)

def cumsum(t):
    total = 0
    cumsum = []
    for t in t:
       total += t
       cumsum.append(total)
    return cumsum

t = [1, 2, 3]
cumsum(t)

def middle(t):
    return t[1:-1]

t = [1, 2, 3, 4]
middle(t)

def chop(t):
    del t[:1]
    del t[:-1]
    return None
t = [1, 2, 3, 4]
chop(t)

def is_sorted(t):
    for i in range(len(t)-1):
        if t[i+1] < t[i]:
            return False  
        else:
            return True

is_sorted([1, 2, 2])
is_sorted(['b', 'a'])
    

def is_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    return (list1 == list2)


is_anagram('stop', 'pots')
is_anagram('different', 'letters')
is_anagram([1, 2, 2], [2, 1, 2])

def has_duplicates(s):
    sort = s[:]
    sort.sort()
    for i in range(len(sort)-1):
        if sort[i] == sort[i+1]:
            return True
        else:
            return False

print(has_duplicates('cba'))
print(has_duplicates('abba'))

def has_adjacent_duplicates(s):
    last = i[0]
    for i in s[1:]:
        if i == last:
            return True
        last = i
    return False

print(has_adjacent_duplicates('cba'))
print(has_adjacent_duplicates('abca'))
print(has_adjacent_duplicates('abbc'))

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()
