data = open('/yellow(easy)/autocorrect/autocorrect-samples/1.in')
data = data.readlines()

d, w = data[1].strip().split()

d = int(d)
w = int(w)

d_words = []
w_words = []

for i in data[2:d+2]:
    i = i.strip()
    d_words.append(i)

for i in data[w:]:
    i = i.strip()
    w_words.append(i)


for i in w_words:
    hamming_dist_list = []
    for j in d_words:
        hamming_dist = 0
        if len(i) == len(j):
            for k in range(len(i)):
                if i[k] != j[k]:
                    hamming_dist += 1
        hamming_dist_list.append(hamming_dist)

    print(d_words[hamming_dist_list.index(max(hamming_dist_list))])








