# ---------------------------------------------
# GUIA DE ANÁLISE DE DADOS COM PYTHON, PANDAS E MATPLOTLIB
# ---------------------------------------------

# 1. IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd                          # Biblioteca principal para manipulação de dados tabulares
import matplotlib.pyplot as plt              # Biblioteca para geração de gráficos simples
import seaborn as sns                        # (Opcional) Gráficos com visual mais bonito
import numpy as np                           # (Opcional) Para cálculos numéricos e estatísticas

# 2. LEITURA DE ARQUIVOS
# CSV
df = pd.read_csv('arquivo.csv')              # Lê arquivo CSV do mesmo diretório

# Excel
# df = pd.read_excel('arquivo.xlsx', engine='openpyxl')

# 3. EXPLORAÇÃO DOS DADOS
print(df.head())                             # Mostra as 5 primeiras linhas
print(df.tail())                             # Mostra as últimas 5 linhas
print(df.columns)                            # Mostra os nomes das colunas
print(df.info())                             # Mostra tipos de dados e valores nulos
print(df.describe())                         # Estatísticas básicas: média, desvio, min, max

# 4. LIMPEZA DE DADOS
print(df.isnull().sum())                     # Conta valores nulos por coluna
df = df.dropna()                             # Remove linhas com valores nulos
# df = df.fillna(0)                          # Preenche valores nulos com 0

# 5. ACESSO A DADOS
print(df['coluna'])                          # Acessa uma coluna
print(df[['coluna1', 'coluna2']])            # Acessa múltiplas colunas
print(df.loc[0])                             # Acessa a linha de índice 0
print(df.iloc[0:5])                          # Acessa da linha 0 até a 4

# 6. FILTRAGEM E CONDIÇÕES
filtro = df[df['idade'] > 30]                # Filtra onde idade > 30
filtro = df[(df['sexo'] == 'F') & (df['idade'] < 40)]  # Filtros múltiplos com AND

# 7. CRIAÇÃO DE NOVAS COLUNAS
df['dobro_salario'] = df['salario'] * 2      # Cria coluna com valores derivados
df['nome_completo'] = df['nome'] + ' ' + df['sobrenome']

# 8. AGRUPAMENTOS E ESTATÍSTICAS
print(df.groupby('departamento')['salario'].mean())  # Média salarial por departamento
print(df.groupby('cidade')['idade'].count())         # Quantidade de pessoas por cidade
print(df['salario'].max())                           # Maior salário
print(df['salario'].sum())                           # Soma total de salários

# 9. ORDENAÇÃO
df = df.sort_values(by='idade', ascending=False)     # Ordena do maior pro menor

# 10. GRÁFICOS SIMPLES COM MATPLOTLIB
# Gráfico de barras
plt.bar(df['produto'], df['vendas'])
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Vendas')
plt.show()

# Gráfico de linha
plt.plot(df['ano'], df['vendas'])
plt.title('Evolução de Vendas')
plt.grid(True)
plt.show()

# Gráfico de pizza
plt.pie(df['vendas'], labels=df['produto'], autopct='%1.1f%%')
plt.title('Distribuição de Vendas')
plt.show()

# Histograma
plt.hist(df['idade'], bins=10)
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# 11. SALVANDO RESULTADOS
df.to_csv('resultado.csv', index=False)      # Salva o DataFrame como CSV

# 12. Conversão de Datas e Criação de Colunas de Tempo
df['data'] = pd.to_datetime(df['data'])        # Converte coluna para datetime
df['ano'] = df['data'].dt.year                 # Extrai o ano
df['mes'] = df['data'].dt.month                # Extrai o mês (numérico)
df['mes_nome'] = df['data'].dt.strftime('%B')  # Nome do mês (Janeiro, Fevereiro...)
df['dia_semana'] = df['data'].dt.day_name()    # Nome do dia da semana

# 13. Resetar índice após agrupamentos ou filtros
df = df.reset_index()                          # Reseta o índice após agrupamento

# 14. Mesclagem e Junção de Dados
df_merged = pd.merge(df1, df2, on='chave', how='inner')  # Junção tipo inner
df_merged = pd.merge(df1, df2, on='chave', how='left')   # Junção tipo left

# 15. Aplicação de Funções Personalizadas
df['faixa'] = df['idade'].apply(lambda x: 'jovem' if x < 30 else 'adulto')

# 16. Análise de Correlação (Seaborn opcional)
print(df.corr(numeric_only=True))              # Correlação entre colunas numéricas
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Mapa de Calor das Correlações')
plt.show()

# Extras
# Tratar duplicatas
df = df.drop_duplicates()                     # Remove linhas duplicadas
# Limpar colunas com espaços ou nomes ruins:
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# Renomear colunas:
df.rename(columns={'old': 'new'}, inplace=True)
# Estatísticas descritivas personalizadas:
df['salario'].median()                        # Mediana
df['idade'].value_counts()                    # Frequência dos valores únicos

