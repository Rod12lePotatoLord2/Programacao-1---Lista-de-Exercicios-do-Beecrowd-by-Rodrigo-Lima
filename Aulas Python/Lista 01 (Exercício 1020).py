# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

x = int(input()) # Representa o total de dias
anos = x // 365  # Representa o cálculo de quantos anos completos cabem no total de dias fornecidos
meses = (x % 365) // 30  # Representa o cálculo de quantos meses restam após os anos, assim calculando o valor de meses completos que cabem no total de dias fornecidos
dias = ((x % 365) % 30) # Representa o cálculo de quantos dias restam após meses e anos, calculando o valor de dias completos que cabem no total de dias fornecidos

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')