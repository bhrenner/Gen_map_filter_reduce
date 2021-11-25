"""
Lê cada linha de um arquivo csv sem utilizar muita memória 
Criar um gerador, que le uma linha por vez de um arquivo csv
transforma em lista
Chama uma função que cria um dicionário
Filtra por data 
e soma todos os crimes
"""
import csv
import function_gen
from functools import reduce

arquivo = open('geradores/reccrimepfa-210902-120414.csv', 'r')
csv_gen = (row for row in arquivo)
linha_lis = (l.rstrip().split(",") for l in csv_gen)
next(linha_lis)
dicio = list(map(function_gen.faz_dicio, linha_lis))
dicio_filtrado = list(filter(lambda ano: ano['Data'].year > 2012,  dicio))
soma_filtrado = reduce(lambda soma, crime: soma + crime['Total'], dicio_filtrado, 0)

print(f'Soma de todos os crimes após o ano de 2012: {soma_filtrado}')

