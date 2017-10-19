#Exercise 1
def my_func(*args): 
    return sum(args)

#Exercise 2 
def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print letter, count
most_frequent(text)

def make_anagram_dict(word_list):
    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)

    result = {fp: result[fp] for fp in result if len(result[fp]) > 1}
    return result
anagrams = make_anagram_dict(words)

def print_anagrams(anagrams):
    """Uses a generator to call and print 5 items from mydict"""
    fp = (fp for fp in anagrams)

    print "Sample from anagram dict:"
    for i in range(1, 6):
        # call once, print twice
        fp_next = fp.next()
        print "%s) %s:" % (i, fp_next), anagrams[fp_next]

    print "..."
    print "\n"

print_anagrams(anagrams)