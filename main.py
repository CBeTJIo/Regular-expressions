import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Разбивка ФИО по ячейкам:
new_list = []
for name_list in contacts_list:
    first_pos = name_list[0].split()
    second_pos = name_list[1].split()
    if len(first_pos) > 2:
        name_list[1] = first_pos[1]
        name_list[2] = first_pos[2]
        name_list[0] = first_pos[0]
    if 1 < len(first_pos) < 3:
        name_list[1] = first_pos[1]
        name_list[0] = first_pos[0]
    if len(second_pos) > 1:
        name_list[2] = second_pos[1]
        name_list[1] = second_pos[0]
    new_list.append(name_list)

# Удаление дублей:
filter_list = []
for enemy in new_list:
    summ = len(new_list)
    while summ > 0:
        summ -= 1
        if enemy[0] == new_list[summ][0] and enemy[1] == new_list[summ][1]:
            if enemy[2] == new_list[summ][2] or enemy[2] == '':
                enemy[2] = new_list[summ][2]
            if enemy[3] == new_list[summ][3] or enemy[3] == '':
                enemy[3] = new_list[summ][3]
            if enemy[4] == new_list[summ][4] or enemy[4] == '':
                enemy[4] = new_list[summ][4]
            if enemy[5] == new_list[summ][5] or enemy[5] == '':
                enemy[5] = new_list[summ][5]
            if enemy[6] == new_list[summ][6] or enemy[6] == '':
                enemy[6] = new_list[summ][6]
    if enemy not in filter_list:
        filter_list.append(enemy)

phones = []
for numbers in filter_list:
    pattern = r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})\.?"
    subbstitution = r"+7(\2)\3-\4-\5"
    result = re.sub(pattern, subbstitution, numbers[5])

    pattern1 = r"\s*.?(\w{3}).?\s*(\d{4}).?"
    subbstitution1 = r" \1.\2"
    result1 = re.sub(pattern1, subbstitution1, result)
    phones.append(result1)

count = len(phones) - 1
while count > 0:
    filter_list[count][5] = phones[count]
    count -= 1

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(filter_list)