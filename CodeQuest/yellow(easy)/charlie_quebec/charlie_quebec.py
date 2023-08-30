data = open('/yellow(easy)/charlie_quebec/charlie-quebec-samples/1.in')
data = data.readlines()

dict = {'a':'alpha',
        'b':'bravo',
        'c':'charlie',
        'd':'delta',
        'e':'echo',
        'f':'foxtrot',
        'g':'golf',
        'h':'hotel',
        'i':'india',
        'j':'juliet',
        'k':'kilo',
        'l':'lima',
        'm':'mike',
        'n':'november',
        'o':'oscar',
        'p':'papa',
        'q':'quebec',
        'r':'romeo',
        's':'sierra',
        't':'tango',
        'u':'uniform',
        'v':'victor',
        'w':'whiskey',
        'x':'xray',
        'y':'yankee',
        'z':'zulu'}

for line in data[1:]:
    word_list = []
    line = line.strip()
    if not line.isdigit():
        line = line.split(' ')
        for i in line:
            for j in range(len(i)):
                if j == len(i)-1:
                    print(dict[i[j].lower()], end='')
                else:
                    print(dict[i[j].lower()], end='-')
            print(end=' ')
        print()


