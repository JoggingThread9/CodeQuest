data = open('/yellow(easy)/caught_speeding/caught-speeding-samples/1.in')
data = data.readlines()

for line in data[1:]:
    line = line.strip().split(' ')
    speed = int(line[0])
    birthday = line[1]

    if birthday == 'true':
        if speed <= 65:
            print('no ticket')
        elif 65 < speed < 85:
            print('small ticket')
        else:
            print('big ticket')
    else:
        if speed <= 60:
            print('no ticket')
        elif 60 < speed < 80:
            print('small ticket')
        else:
            print('big ticket')
