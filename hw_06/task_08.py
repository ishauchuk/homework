# 8) В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.

string = 'mother father sister and brother'
data = string.split(' ')
data_1 = data [::-1]
data_2 = ' '.join(data_1)
print(data_2)