"""Advent of code. Day 1"""

l_lst, r_lst = [], []

with open('day_1/input.txt', 'r', encoding='UTF-8') as input_file:
    for line in input_file:
        l_num, r_num = map(int, line.split())
        l_lst.append(l_num)
        r_lst.append(r_num)

diff_list = []
l_lst.sort(), r_lst.sort()
for i in range(len(l_lst)):
    diff_list.append(abs(l_lst[i] - r_lst[i]))

print(sum(diff_list))
