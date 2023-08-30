data = open('/yellow(easy)/bigger_is_better/bigger-is-better-samples/1.in')
data = data.readlines()

for line in data[1:]:
    line = line.strip().split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])

    largest = line[0]
    for i in line:
        if largest < i:
            largest = i

    print(largest)

