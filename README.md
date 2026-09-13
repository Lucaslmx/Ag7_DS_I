# 💧 Classificação do Consumo de Água

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-repositório-181717?logo=github&logoColor=white)](https://github.com/Lucaslmx/Ag7_DS_I)
[![Água](https://img.shields.io/badge/Água-consumo%20consciente-2F80ED)](#)
[![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-alertas%20educativos-27AE60)](#)

Programa simples em Python para classificar o perfil de consumo de água de um imóvel e emitir um alerta educativo conforme o tipo de imóvel e o consumo mensal informado.

O código executável está disponível em [`consumo-agua/app.py`](consumo-agua/app.py).

## 🎯 Objetivo

Solicitar o tipo de imóvel e o consumo mensal de água em metros cúbicos, aplicar as regras de negócio da companhia de saneamento e exibir a orientação correspondente ao morador.

## 📋 Regras de classificação

| Condição | Mensagem exibida |
| --- | --- |
| Imóvel comercial | Tarifa comercial aplicada - consulte o plano corporativo. |
| Apartamento com consumo menor que 10 m³ | Consumo econômico - excelente controle de água! |
| Apartamento ou casa com consumo residencial de até 25 m³ | Consumo moderado - dentro do padrão residencial. |
| Qualquer outra situação | Consumo excessivo - adote medidas de economia e verifique vazamentos. |

As condições são avaliadas na ordem apresentada. Na regra da atividade, a condição de consumo moderado utiliza `or`: todo apartamento que não entrar na primeira classificação residencial é direcionado para essa mensagem; para casas, o limite considerado é de 25 m³.

## 🧠 Conceitos utilizados

- Entrada de dados com `input()`.
- Conversão do consumo para `float`.
- Normalização do tipo de imóvel com `strip()` e `lower()`.
- Operadores relacionais, como `<` e `<=`.
- Operadores lógicos `and` e `or`.
- Estrutura de decisão `if`, `elif` e `else`.
- Validação de dados informados pelo usuário.

## ▶️ Como executar

É necessário ter o Git e o Python instalados.

No terminal, baixe o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/Lucaslmx/Ag7_DS_I.git
cd Ag7_DS_I/consumo-agua
```

Execute o programa com:

```bash
python app.py
```

No Windows, também é possível usar:

```bash
py app.py
```

O programa não utiliza bibliotecas externas.

## 💡 Exemplos

### Imóvel comercial

```text
Qual é o tipo de imóvel? (comercial, casa ou apartamento): comercial
Qual é o consumo mensal de água? (m³): 80

💧------ Classificação do Consumo de Água ------💧
Tipo de imóvel: Comercial
Consumo mensal: 80.00 m³
Alerta: Tarifa comercial aplicada - consulte o plano corporativo.
💧----------------------------------------------💧
```

### Apartamento com consumo econômico

```text
Qual é o tipo de imóvel? (comercial, casa ou apartamento): apartamento
Qual é o consumo mensal de água? (m³): 8,5

💧------ Classificação do Consumo de Água ------💧
Tipo de imóvel: Apartamento
Consumo mensal: 8.50 m³
Alerta: Consumo econômico - excelente controle de água!
💧----------------------------------------------💧
```

### Casa com consumo moderado

```text
Qual é o tipo de imóvel? (comercial, casa ou apartamento): casa
Qual é o consumo mensal de água? (m³): 25

💧------ Classificação do Consumo de Água ------💧
Tipo de imóvel: Casa
Consumo mensal: 25.00 m³
Alerta: Consumo moderado - dentro do padrão residencial.
💧----------------------------------------------💧
```

### Casa com consumo excessivo

```text
Qual é o tipo de imóvel? (comercial, casa ou apartamento): casa
Qual é o consumo mensal de água? (m³): 30

💧------ Classificação do Consumo de Água ------💧
Tipo de imóvel: Casa
Consumo mensal: 30.00 m³
Alerta: Consumo excessivo - adote medidas de economia e verifique vazamentos.
💧----------------------------------------------💧
```

## 📁 Estrutura do projeto

```text
Ag7_DS_I/
├── README.md
└── consumo-agua/
    └── app.py
```
