from math import pi

data = open('/yellow(easy)/around_and_around/around-and-around-samples/1.in')
data = data.readlines()

circum = 40075

r = circum / (2*pi)


for oR in data[1:]:
    oR = oR.strip()
    oR = int(oR)
    print(round(2 * pi * (r + oR), 1))
