#Inportacao de bibliotecas
    #pandas para lidar com o arquivo csv 
    #matplot.pyplot as plt para gerar o grafico propriamente dito ...o as plt serve para apelidade e nao precisar ficar chamando de matplot.pyplot toda vez
    #mplcursors gera as legenda no cursor
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Carregar os dados do arquivo CSV
    #o metodo read_csv() contido na biblioteca pandas que esta renomeada como pd,serve para carregar o arquivo csv no objeto df (basicamente carrega na memoria)
df = pd.read_csv('dados.csv')

# Criar o gráfico
    #
plt.figure(figsize=(10, 6))

# Plotar cada coluna, exceto a coluna "Ano" para ter algo dinamico ...aqui eu posso colocar mas colunas que seriam automaticamente adicionadas novas linhas ao grafico
for coluna in df.columns[1:]:
    plt.plot(df['Ano'], df[coluna], marker='o', linestyle='-', label=coluna)

# Adicionar título e rótulos aos eixos
plt.title('População Mundial por Faixa Etária (1950-2100)')
plt.xlabel('Ano')
plt.ylabel('População (bilhões)')

# Adicionar grid e legenda
plt.grid(True)
plt.legend()

# Adicionar interatividade
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()} ({int(sel.target[0])}): {sel.target[1]:.2f} bilhões'))

# Mostrar o gráfico
plt.show()
