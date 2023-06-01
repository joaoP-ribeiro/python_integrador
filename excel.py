import pandas as pd

def excel(nome, fabricante, valor):
    coluna_valor = {"Nome": nome, "Fabricante": fabricante, "Valor": valor}
    dados = pd.DataFrame(data=coluna_valor)
    return dados


