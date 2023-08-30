data = open('/yellow(easy)/AEIOU/aeiou-samples/1.in')
data = data.readlines()

n_samples = data[0]

vowels = ['a', 'e', 'i', 'o', 'u']

for line in data[1:]:
    line = line.strip()
    count = 0
    for i in line:
        if i in vowels:
            count += 1
    print(count)


