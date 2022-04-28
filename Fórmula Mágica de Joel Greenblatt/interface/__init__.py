from time import sleep


def linha(tam=80):
    return '-' * tam

def cabeçalho(txt):
    sleep(1.5)
    print(linha())
    print(txt.center(80))
    print(linha())
    sleep(2)
