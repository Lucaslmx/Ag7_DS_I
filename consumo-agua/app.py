# Arquivo: app.py
# Classificação do consumo de água - Agenda 07 - Desenvolvimento de Sistemas I

# --- 1. Entrada de Dados ---
# Recebe o tipo de imóvel e o consumo mensal de água.
tipo_imovel = input("Qual é o tipo de imóvel? (comercial, casa ou apartamento): ").strip().lower()
consumo_mensal = float(input("Qual é o consumo mensal de água? (m³): ").strip().replace(",", "."))

# --- 2. Validação ---
# Verifica se o tipo de imóvel é válido e se o consumo não é negativo.
if tipo_imovel not in ("comercial", "casa", "apartamento") or consumo_mensal < 0:
	print("\nValor inválido: confira o tipo de imóvel e o consumo informado.")
else:
	# --- 3. Classificação do Consumo ---
	# Aplica as regras de negócio na ordem apresentada na atividade.
	if tipo_imovel == "comercial":
		mensagem = "Tarifa comercial aplicada - consulte o plano corporativo."
	elif tipo_imovel == "apartamento" and consumo_mensal < 10:
		mensagem = "Consumo econômico - excelente controle de água!"
	elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo_mensal <= 25):
		mensagem = "Consumo moderado - dentro do padrão residencial."
	else:
		mensagem = "Consumo excessivo - adote medidas de economia e verifique vazamentos."

	# --- 4. Saída de Dados ---
	# Exibe os dados informados e o alerta correspondente.
	print("\n💧------ Classificação do Consumo de Água ------💧")
	print(f"Tipo de imóvel: {tipo_imovel.title()}")
	print(f"Consumo mensal: {consumo_mensal:.2f} m³")
	print(f"Alerta: {mensagem}")
	print("💧----------------------------------------------💧")
