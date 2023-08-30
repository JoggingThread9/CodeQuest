data = open('/yellow(easy)/animal_farm/animal-farm-samples/1.in')
data = data.readlines()

turkeys = 2
goats = 4
horses = 4

for line in data[1:]:
    line = line.strip()
    line = line.split(' ')

    for i in range(len(line)):
        line[i] = int(line[i])

    num = 0
    num += line[0] * turkeys
    num += line[1] * goats
    num += line[2] * horses

    print(num)



