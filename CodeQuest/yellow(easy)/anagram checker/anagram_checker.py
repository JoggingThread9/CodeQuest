data = open('/yellow(easy)/anagram checker/anagram-checker-samples/1.in')
data = data.readlines()

n_samples = data[0]


for line in data[1:]:
    line = line.strip()
    line_list = line.split('|')

    word = line_list[0]
    word = list(word)
    anagram = line_list[1]
    anagram = list(anagram)

    is_anagram = None
    for i in word:
        if word == anagram:
            is_anagram = 'NOT AN ANAGRAM'
            break
        elif i in anagram:
            anagram.remove(i)
            is_anagram = 'ANAGRAM'
        else:
            is_anagram = 'NOT AN ANAGRAM'
            break

    print(line + ' = ' + is_anagram)













