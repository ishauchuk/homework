# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.

def generate(lst):
    a = [f'{i} - {string}' for i, string in enumerate(lst)]
    return a


print(generate(['a', 'b']))