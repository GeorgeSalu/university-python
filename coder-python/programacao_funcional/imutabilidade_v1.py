#!/usr/local/bin/python3
from locale import setlocale, LC_ALL
from calendar import month_name
from functools import reduce

# portuguues do Brasil
setlocale(LC_ALL, 'pt_BR')

# listar todos os meses do ano com 31 dias