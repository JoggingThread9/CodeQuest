data = open('/yellow(easy)/color_wheel/color-wheel-samples/1.in')
data = data.readlines()

color_wheel = ['red', 'red-violet', 'violet', 'blue-violet', 'blue', 'blue-green', 'green', 'yellow(easy)-green', 'yellow(easy)', 'yellow(easy)-orange', 'orange', 'red-orange']
primary_colors = ['red', 'blue', 'yellow(easy)']

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for color in data[1:]:
    color = color.strip()
    if color in primary_colors:
        print(f'No colors need to be mixed to make {color}')
    elif '-' in color:
        color_1 = color_wheel[(color_wheel.index(color) + 1) % len(color_wheel)]
        color_2 = color_wheel[(color_wheel.index(color) - 1) % len(color_wheel)]
        if alphabet.index(color_1[0]) < alphabet.index(color_2[0]):
            print(f'In order to make {color}, {color_1} and {color_2} must be mixed')
        else:
            print(f'In order to make {color}, {color_2} and {color_1} must be mixed')

    else:
        color_1 = color_wheel[(color_wheel.index(color) + 2) % len(color_wheel)]
        color_2 = color_wheel[(color_wheel.index(color) - 2) % len(color_wheel)]
        if alphabet.index(color_1[0]) < alphabet.index(color_2[0]):
            print(f'In order to make {color}, {color_1} and {color_2} must be mixed')
        else:
            print(f'In order to make {color}, {color_2} and {color_1} must be mixed')

