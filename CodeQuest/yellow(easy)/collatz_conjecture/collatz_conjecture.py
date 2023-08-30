data = open('/yellow(easy)/collatz_conjecture/collatz-conjecture-samples/1.in')
data = data.readlines()

for num in data[1:]:
    num = int(num.strip())
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        sequence.append(num)

    print(f'{sequence[0]}:{len(sequence)}')
