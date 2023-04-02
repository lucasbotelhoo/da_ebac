import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv', sep=',')

grafico = sns.lineplot(data=df, x='dia', y='venda')
grafico.set(title='Média do Preço da Gasolina',xlabel='dia',ylabel='price');
plt.savefig('gasolina.png')