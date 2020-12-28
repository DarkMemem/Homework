input_data = 'В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте.'
words_counter = {}
for word in input_data.split():
    try:
        words_counter[word] += 1
    except KeyError:
        words_counter[word] = 1
print(words_counter)
