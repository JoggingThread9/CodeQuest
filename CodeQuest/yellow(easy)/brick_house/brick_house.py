data = open('/yellow(easy)/brick_house/brick-house-samples/1.in')
data = data.readlines()

for line in data[1:]:
    line = line.strip().split(' ')
    if int(line[0]) + 5*int(line[1]) == int(line[2]):
        print('true')
    elif int(line[0]) == int(line[2]):
        print('true')
    elif 5*int(line[1]) == int(line[2]):
        print('true')
    else:
        print('false')
