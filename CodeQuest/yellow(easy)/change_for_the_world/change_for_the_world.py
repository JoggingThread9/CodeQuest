data = open('/yellow(easy)/change_for_the_world/change-for-the-world-samples/1.in')
data = data.readlines()

quarter = .25
dime = .1
nickel = .05
pennie = .01


def print_ans(n_quarters, n_dimes, n_nickels, n_pennies, line):
    print('$' + line)
    print(f'Quarters={n_quarters}')
    print(f'Dimes={n_dimes}')
    print(f'Nickels={n_nickels}')
    print(f'Pennies={n_pennies}')


for line in data[1:]:
    line = line.strip()
    line = line[1:]
    amount = float(line)

    n_quarters = str(amount / quarter)
    n_quarters = n_quarters.split('.')
    n_quarters = int(n_quarters[0])

    amount -= n_quarters * quarter

    n_dimes = str(amount / dime)
    n_dimes = n_dimes.split('.')
    n_dimes = int(n_dimes[0])

    amount -= n_dimes * dime

    n_nickels = str(amount / nickel)
    n_nickels = n_nickels.split('.')
    n_nickels = int(n_nickels[0])

    amount -= n_nickels * nickel

    n_pennies = str(amount / pennie)
    n_pennies = n_pennies.split('.')
    n_pennies = int(n_pennies[0])

    print_ans(n_quarters, n_dimes, n_nickels, n_pennies, line)