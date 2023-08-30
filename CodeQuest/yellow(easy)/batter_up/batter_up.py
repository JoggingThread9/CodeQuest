data = open('/yellow(easy)/batter_up/batter-up-samples/1.in')
data = data.readlines()

for line in data[1:]:
    line = line.strip().split(':')
    player = line[0]
    bats = line[1]
    bats = bats.split(',')

    total = len(bats)-bats.count('BB')

    slg = (1*bats.count('1B') + 2*bats.count('2B') + 3*bats.count('3B') + 4*bats.count('HR')) / total
    print(f'''{player}={round(slg, 3)}''')
