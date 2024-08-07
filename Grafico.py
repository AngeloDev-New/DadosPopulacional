
#!pip install mplcursors
#Importacao de bibliotecas
    #pandas para lidar com o arquivo csv 
    #matplot.pyplot as plt para gerar o grafico propriamente dito ...o as plt serve para apelidade e nao precisar ficar chamando de matplot.pyplot toda vez
    #mplcursors gera as legenda no cursor
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Carregar os dados do arquivo CSV
    #o metodo read_csv() contido na biblioteca pandas que esta renomeada como pd,serve para carregar o arquivo csv no objeto df (basicamente carrega na memoria)
    #no caso deste arquivo ele esta puxando diretamente do repositorio do github
    #o pandas puxa tanto do proprio computador "c:\pasta_teste\arquivo.csv" quanto da internet como abaixo
df = pd.read_csv('https://raw.githubusercontent.com/AngeloDev-New/DadosPopulacional/main/dados.csv')

# Criar o gráfico
    #
plt.figure(figsize=(10, 6))

# Plotar cada coluna, exceto a coluna "Ano" para ter algo dinamico ...aqui eu posso colocar mas colunas que seriam automaticamente adicionadas novas linhas ao grafico
for coluna in df.columns[1:]:
    #este "for" percorrera toda coluna existente apos a primeira 
    #logo a cada ciclo ele vai plotar uma linha 
    #quando usamos df[nome] retornamos um objeto chamdo series que e algo similar a listas porem com metodos proprios do pandas
    #o primeiro argumento fica fixo na coluna ano df["ano"] sendo assim retorna os anos presente no csv 1950-2100
    #o segundo argumento capta a coluna do cicli...primeiro ciclo segunda coluna e assim por diante
    #esses 2 forman um x,y no plano cartesiano e como sao listas trassam uma reta
    #marker representa o estilo dos pontos da reta sendo "o" uma bolinha "s" um quandrado "+" um simbolo de + ...
    #linestyle representa o estilo da reta sendo "- ou solid" uma linha, "dotted" linha pontilhada,"dashed" linha tracejada,"dashdot" linha traço ponto ...alen de perssonalizados com tuplas mas n entrei mto afundo
    #pelo que entendi o color e aleatorio quando nao definido ...mas para definir manualmente podemos usar o parametro color ex:
    #plt.plot(x,y,color="red")
    """
    cores predefinidas "b" ou "Blue", "k" ou preto enfim so da um google
    cores hexadecimal "#ffd555" uma string contendo o hexadecimal
    cores RGB (0.1,0.5,0.8) uma tupla com os valores de r g b 

    """
    plt.plot(df['Ano'], df[coluna], marker='o', linestyle='dotted', label=coluna)

# Adicionar título e rótulos aos eixos
plt.title('População Mundial por Faixa Etária (1950-2100)')
plt.xlabel('Ano')
plt.ylabel('População (bilhões)')

# Adicionar grid e legenda
plt.grid(True)
plt.legend()

# Adicionar interatividade
cursor = mplcursors.cursor(hover=True)

"""
LAMBDA's servem para escrever funcoes anonimas sem precisar escrever muito
a funcao abaixo por exemplo poderia ser escrida da seguinte maneira

def funcaoquenaoelambda(sel):
    nome_da_linha = self.artist.get_label()
    ano = int(sel.target[0])
    quantidade = sel.target[1]:.2f 
    sel.anotation.set_text(f'{nome_da_linha}({ano}):{quantidade} bilhoes')
e na chamada ser chamado assim 

cursor.connect("add",funcaoquenaoelambda)
"""
#cursor se "conecta ao grafioco e basicamente essa funcao lambda pega o objeto 'sel' que e a interface com a legenda concatena uma string e seta a mesma"
#quando queremos concatenar uma string a variaveis usamos f'' antes da string assim se colocarmos {variavel} dentro da string o interpretador junta tudo
#                 escreva_na_legenda(f'    {nome_da_linha}              ({ano})      ):    {quantidade}     bilhoes')
#lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()} ({int(sel.target[0])}): {sel.target[1]:.2f} bilhões')
cursor.connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()} ({int(sel.target[0])}): {sel.target[1]:.2f} bilhões'))

# Mostrar o gráfico
plt.show()
