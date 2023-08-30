data = open('/yellow(easy)/anti_asteroid/anti-asteroid-weapon-samples (1)/1.in')
data = data.readlines()

for line in range(1, len(data[1:])):
    check = data[line].strip()
    check = check.split(' ')
    if len(check) == 1:
        cord_list = []
        dist_list = []
        for i in range(line+1, line+int(check[0])+1):
            cord_set = data[i].strip()
            cord_set = cord_set.split(' ')
            cord_list.append(cord_set)
        for i in cord_list:
            dist = 0
            for j in i:
                dist += int(j)**2
            dist_list.append(dist**.5)

        for i in range(len(dist_list)):
            for j in range(len(dist_list)):
                if dist_list[i] < dist_list[j]:
                    dist_list[i], dist_list[j] = dist_list[j], dist_list[i]
                    cord_list[i], cord_list[j] = cord_list[j], cord_list[i]

        for i in cord_list:
            for j in i:
                print(j, end=' ')
            print('')

"""
loop through until you hit the number that says how many asteriods are there
go through all those values calculate the distaces
sort them
print the sorted distance coordinates
move on
"""

