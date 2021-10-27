import re
from operator import length_hint
# по непонятной причине обычный len(list) выдает ошибку
with open("Poil_contig.fa", 'r') as f:
    str_list = f.readlines()
    head_list = []
    for i in range(length_hint(str_list)):
        if '>' in str_list[i]:
            head_list.append(str_list[i])
    limb_list = []
    for i in head_list:
        regex = re.compile("\_(.*)\_")
        limb_list.append(regex.findall(i)[0])
    num_list = []
    for i in limb_list:
        num_list.append(int(i[3:]))
    num_list.sort(reverse=True)
    print('Число контигов: ', length_hint(num_list))
    print('Длина собранного генома: ', sum(num_list))
    all_sum = sum(num_list)
    current_sum = 0
    for i in num_list:
        current_sum += i
        if current_sum >= all_sum * 0.5:
            N50 = i
            break
    print('N50: ', i)
