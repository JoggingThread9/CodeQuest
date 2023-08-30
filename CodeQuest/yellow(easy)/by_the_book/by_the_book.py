data = open('/yellow(easy)/by_the_book/by-the-book-samples/1.in')
data = data.readlines()

for line in data[1:]:
    line = line.strip()

    num = 0
    multiple = 0
    count = 0

    for i in range(8+1):
        num += (int(line[i]) * (10 - i))

    while multiple < num:
        count += 1
        multiple = count * 11

    remainder = multiple - num

    if str(remainder) == line[-1]:
        print('valid')
    elif line[-1] == 'X':
        if remainder == 10:
            print('valid')
    else:
        print('invalid')

