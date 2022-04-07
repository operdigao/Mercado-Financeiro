# Calcula o CAPM de um ativo

rf = float(input('Qual é a taxa livre de risco? '))
bi = float(input('Qual é o beta do investimento? '))
erm = float(input('Qual é o retorno esperado do mercado? '))
premioderisco = erm-rf
eri = rf + (bi*(premioderisco))

print(f'Retorno esperado do ativo é {eri:.2f}')

