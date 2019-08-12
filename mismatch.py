import random

f_hi = open("hi.csv", "r")
hi_content = [line for line in f_hi.readlines() if 'null' not in line.split(";")]
# hi_content = f_hi.readlines()

f_mr = open("mr.csv", "r")
mr_content = [line for line in f_mr.readlines() if 'null' not in line.split(";")]
# mr_content = f_mr.readlines()

hi_content = [x.split(';') for x in hi_content]
mr_content = [x.split(';') for x in mr_content]

f_mismatched = open("hi_mr1.csv", "w+")

sample_data = random.sample(range(0,30000), 1000)
sample_hi = sample_data[0:500]
sample_mr = sample_data[500:1000]
for hi, mr in zip(sample_hi, sample_mr):
    # hi_word = hi_content[i][1]
    # mr_word = mr_content[i+100][1]

    # if ',' in hi_content[i][1]:
    #     hi_word = hi_content[i][1].split(",")[0]
    
    # if ',' in mr_content[i+100][1]:
    #     mr_word = mr_content[i+100][1].split(",")[0]

    hi_word = hi_content[hi][1].split(",")
    mr_word = mr_content[mr][1].split(",")
    flag = 0
    for w in hi_word:
        if w in hi_content[hi][3]:
            flag = 1
            hi_word = w
            print("hi_id = ", hi)
            print("hi_word = ", hi_word)
            print("hi_example = ", hi_content[hi][3])
            break
    if flag == 0:
        hi_word = hi_word[0]
    else:
        flag = 0
    for w in mr_word:
        if w in mr_content[mr][3]:
            flag = 1
            mr_word = w
            print("mr_id = ", mr)
            print("mr_word = ", mr_word)
            print("mr_example = ", mr_content[mr][3])
            break
    if flag == 0:
        mr_word = mr_word[0]
    
    row = hi_content[hi][0] + ";" + hi_content[mr][0] + ";" + hi_word + ";" + mr_word + ";" + hi_content[hi][2] + ";" + mr_content[mr][2] + ";" + hi_content[hi][3] + ";" + mr_content[mr][3] + "\n"
    f_mismatched.write(row)

f_mismatched.close()
