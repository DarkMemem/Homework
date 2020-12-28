text = input("Введите текст: ")
words = text.split(" ")
count_mapping = {}
for j in words:
    count_mapping.setdefault(j, 0)
    count_mapping[j] += 1
if all(v == 1 for v in count_mapping.values()):
    print("В тексте отсуствуют повторяющиеся слова.")
else:
    for word, count in count_mapping.items():
        if count > 1:
            print(word, "->", count)
