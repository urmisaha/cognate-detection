import random

f_hi = open("hi.csv", "r")
hi_content = [line for line in f_hi.readlines() if 'null' not in line.split(";")]   # not considering sentences containing null values

f_mr = open("mr.csv", "r")
mr_content = [line for line in f_mr.readlines() if 'null' not in line.split(";")]   # not considering sentences containing null values

hi_content = [x.split(';') for x in hi_content]                                     # splitting columns
mr_content = [x.split(';') for x in mr_content]                                     # splitting columns

f_mismatched = open("hi_mr.csv", "w+")

total_len = min(len(hi_content), len(mr_content))
if total_len%2 == 1:
    total_len -= 1

sample_data = random.sample(range(0, total_len), 2000)                                   # 
sample_hi = sample_data[0:1000]
sample_mr = sample_data[1000:2000]

print("file   |   id   |   word    |   example")
print("---------------------------------------------------------------------------------------")
for hi, mr in zip(sample_hi, sample_mr):
    hi_word = hi_content[hi][1].split(",")
    mr_word = mr_content[mr][1].split(",")

    flag = 0
    for w in hi_word:
        if w in hi_content[hi][3]:
            flag = 1
            hi_word = w
            break
    if flag == 0:
        hi_word = hi_word[0]
        print("Hindi:   ", hi_content[hi][0], "   |   ", hi_word, " |   ", hi_content[hi][3])
        continue
    else:
        flag = 0

    for w in mr_word:
        if w in mr_content[mr][3]:
            flag = 1
            mr_word = w
            break
    if flag == 0:
        mr_word = mr_word[0]
        print("Marathi:  ", mr_content[mr][0], "   |   ", mr_word, " |   ", mr_content[mr][3])
        continue
    
    row = hi_content[hi][0] + ";" + mr_content[mr][0] + ";" + hi_word + ";" + mr_word + ";" + hi_content[hi][2] + ";" + mr_content[mr][2] + ";" + hi_content[hi][3] + ";" + mr_content[mr][3] + "\n"
    f_mismatched.write(row)

f_mismatched.close()
