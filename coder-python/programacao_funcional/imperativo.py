#!/usr/local/bin/python3
# listar todos os meses do ano com 31 dias
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Portuguese do Brasil
setlocale(LC_ALL, 'pt_BR')

# lista todos os meses do ano com 31 dias
print('meses com 31 dias')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')