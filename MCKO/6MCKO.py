from itertools import product

for i, x in enumerate(product('авенс', repeat=4), 1):
    s = ''.join(x)
    if 'е' not in s and 'аа' not in s:
        print(i)
        break


# from itertools import product
#
# # product делает все слова, enumerate нумерует их с 1 (i-номер, x-слово)
# for i, x in enumerate(product('авенс', repeat=4), 1):
#     s = ''.join(x)                     	            # Склеиваем буквы в строку
#     if 'е' not in s and 'аа' not in s: 	            # Условия: нет 'е' и нет 'аа'
#         print(i)                       	            # Печатаем номер
#         break                                      	# Стоп, нашли первое!





# int('0101', 5)   # 26 — из пятеричной
# int('0101', 2)   # 5  — из двоичной
# int('FF', 16)    # 255 — из шестнадцатеричной