import paddle
import paddle.nn as nn
import paddle.optimizer as optim
import numpy as np
import pandas as pd   
from sklearn.preprocessing import LabelEncoder, StandardScaler



data = {
    "Bairro": ["Vila Nova Conceição", "Cidade Jardim", "Jardim Paulistano", "Ibirapuera",
               "Vila Olímpia", "Moema", "Itaim Bibi", "Pinheiros", "Jardim Europa", "Brooklin"],
    "Valor_m2": [20500, 25270, 22651, 21428, 18859, 16730, 16000, 14152, 14000, 12500]
}
df = pd.DataFrame(data)

def calcular_preco(bairro, metros):
    if bairro not in df["Bairro"].values:
        return None, "Bairro não encontrado."
    valor_m2 = df.loc[df["Bairro"] == bairro, "Valor_m2"].values[0]
    preco_calculado = valor_m2 * metros
    return preco_calculado, None

def validar_calculo(bairro, metros, preco_estimado):
    preco_calculado, erro = calcular_preco(bairro, metros)
    if erro:
        return erro
    diferenca = abs(preco_calculado - preco_estimado)
    if diferenca < preco_calculado * 0.01:
        return f"Validação OK: cálculo {preco_calculado:,.2f} dentro da margem do estimado {preco_estimado:,.2f}."
    else:
        return f"Atenção: diferença entre cálculo {preco_calculado:,.2f} e estimativa {preco_estimado:,.2f}."

# Uso simplificado:
bairro_input = input("Digite o bairro (ex: Vila Nova Conceição): ")
metros_input = float(input("Digite a metragem (m²): "))

preco, erro = calcular_preco(bairro_input, metros_input)
if erro:
    print(erro)
else:
    print(f"Preço estimado: R$ {preco:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.'))
    msg_validacao = validar_calculo(bairro_input, metros_input, preco)
    print(msg_validacao)
