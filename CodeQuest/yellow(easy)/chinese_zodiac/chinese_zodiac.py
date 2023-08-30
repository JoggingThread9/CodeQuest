data = open('/yellow(easy)/chinese_zodiac/chinese-zodiac-samples/1.in')
data = data.readlines()

yy = None
elements = ['wood', 'fire', 'earth', 'metal', 'water']
animals = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'goat', 'monkey', 'rooster', 'dog', 'pig']

for line in data[1:]:
    year = int(line.strip())
    if year % 2 == 0:
        yy = 'Yang'
    else:
        yy = 'Yin'

    year -= 4

    element = year % 10
    element /= 2
    element = str(element).split('.')
    element = int(element[0])
    element = elements[element]

    animal = year % 12
    animal = animals[animal]

    print(str(year+4) + ' ' + yy + ' ' + element + ' ' + animal)


'''
Five Elements - Wood, Fire, Earth, Metal, Water
o Subtract 4 from the year
o Divide that value by 10 and take the remainder
o Divide that value by 2, and round down to the nearest integer (e.g. 7 / 2 = 3.5, which
rounds down to 3)
o Use that value to locate the element from the list above (Wood = 0, Fire = 1, etc.)
• 12 Animals - Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig
o Subtract 4 from the year
o Divide that value by 12 and take the remainder
o Use the remainder to locate the animal from the list above (Rat = 0, Ox = 1,
'''

