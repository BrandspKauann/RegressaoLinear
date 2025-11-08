# 🏙️ Estimativa de Preço de Imóveis com Regressão Linear
Utilizando PaddlePaddle (China) e conceitos básicos de Machine Learning
# 📘 Visão Geral

Este projeto demonstra, de forma prática e objetiva, como aplicar regressão linear para estimar o preço de imóveis em diferentes bairros de São Paulo.
A ideia central é aproximar o valor de mercado de um imóvel a partir do preço médio do metro quadrado em cada região — tudo implementado de maneira clara e acessível.

Embora simples, o projeto ilustra como a base da inteligência artificial pode ser usada para criar modelos preditivos úteis, mesmo sem grandes volumes de dados.

# 🧠 Objetivo

Criar um sistema que:

Receba como entrada o bairro e a metragem (m²) de um imóvel;

Calcule automaticamente o preço estimado com base no valor médio do metro quadrado daquele bairro;

Realize uma validação automática para verificar se o cálculo está dentro da margem aceitável do preço estimado.

# 🏗️ Estrutura do Projeto

O código é dividido em três partes principais:

1. Base de Dados Simplificada

Uma pequena base foi criada manualmente com 10 bairros de São Paulo e seus respectivos valores médios de m².
Essa base serve como referência para o modelo fazer previsões sem depender de bancos de dados externos.

2. Função de Cálculo do Preço

A função principal recebe o bairro e a metragem do imóvel, consulta o valor médio do m² e retorna o preço estimado.
Caso o bairro não exista na base, o sistema retorna uma mensagem informando que ele não foi encontrado.

3. Função de Validação

Após calcular o preço, o sistema realiza uma checagem simples comparando o valor calculado com uma estimativa fornecida.
Se a diferença estiver dentro de 1%, o cálculo é considerado válido; caso contrário, o sistema alerta que há uma divergência.

# 💬 Exemplo de Funcionamento

O usuário informa:

Bairro: Vila Nova Conceição

Metragem: 120 m²

O sistema localiza o valor médio do metro quadrado para o bairro informado.

Calcula automaticamente o preço estimado:
R$ 2.460.000,00

Em seguida, realiza a validação e retorna uma mensagem confirmando a precisão do cálculo.

# 🧩 Tecnologias Utilizadas

Python 3 — linguagem base do projeto

Pandas e NumPy — manipulação de dados e cálculos numéricos

PaddlePaddle — framework chinês de aprendizado de máquina (importado para futuras expansões do modelo)

Scikit-Learn — para pré-processamento e padronização de dados
