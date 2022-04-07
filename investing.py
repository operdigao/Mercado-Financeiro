# -*- coding: utf-8 -*-
# Investing.com
# Instalação de bibliotecas

import investpy

"""# Calendário Econômico"""

touro = ['medium', 'high']
paises = ['brazil','united states','euro zone','germany']
print(investpy.economic_calendar(time_zone="GMT -3:00", countries=paises, importances=touro))
print('DIVIDENDOS')
print(investpy.get_stock_dividends('PETR4','brazil'))