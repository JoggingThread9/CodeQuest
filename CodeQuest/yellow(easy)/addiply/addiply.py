
data = open('/yellow(easy)/addiply/addiply-samples/1.in')
data = data.readlines()

ans_list = []

n_of_samples = data[0]


for line in data[1:]:
    num_list = []
    curr_ans = []
    for i in line:
        if str.isdigit(i):
            num_list.append(int(i))

    ans = 0
    for i in num_list:
        ans += i
    curr_ans.append(ans)

    ans = 1
    for i in num_list:
        ans *= i
    curr_ans.append(ans)

    for i in curr_ans:
        print(i, end=' ')
    print("")



