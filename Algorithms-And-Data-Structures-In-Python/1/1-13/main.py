# Дана строка-предложение. Подсчитайте вхождение каждого слова в данное предложение.

string = 'abc abc abc abc adb qwerty'
words = string.split()
uniqueWords = set(words)
for word in uniqueWords:
    count = words.count(word)
    print(f'Слово {word} входит в строку {count} раза')
