file = open('src_14.txt', encoding='UTF-8')
res = open('dst.txt', 'wt', encoding='UTF-8')

avr_class = 0
cnt = 0
temp = '{:<25}{:5}'
for line in file:
    temp = '{:<25}{:5}'
    line = line.split()
    name = line[1] + ' ' + line[0][0] + '.'
    arv = round(sum([int(s) for s in line[2:]]) / len(line[2:]), 2)
    if arv < 5:
        print(temp.format(name, arv))

    res.write(temp.format(name, arv))
    res.write('\n')
    avr_class += arv
    cnt += 1


file.close()
res.close()
print(temp.format('Class average:', round(avr_class/cnt, 2)))
