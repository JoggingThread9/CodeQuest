data = open('/yellow(easy)/are_you_a_spy/are-you-a-spy-samples/1.in')
data = data.readlines()

for line in data[1:]:
    line = line.strip()
    line = line.split('|')
    for i in range(len(line)):
        line[i] = line[i].split(' ')

    phrase_1 = line[0]
    phrase_2 = line[1]

    letters_1 = []
    letters_2 = []

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    spy = True

    for i in phrase_1:
        for j in i:
            #j = j.lower()
            if j in alphabet:
                letters_1.append(j)

    for i in phrase_2:
        for j in i:
            #j = j.lower()
            if j in alphabet:
                letters_2.append(j)

    #print(phrase_1)
    #print(phrase_2)
    #print(letters_1)
    #print(letters_2)

    for i in letters_1:
        if i in letters_2:
            #letters_2.remove(i.lower())
            spy = True
        else:
            spy = False

    if spy:
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")

