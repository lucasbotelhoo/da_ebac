import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r'/content/da_ebac/gasolina.csv',sep = ',')

grafico = sns.barplot(data=df, x='dia', y='venda', ci=None, palette='deep')
grafico.set(title='Média do Preço da Gasolina',xlabel='dia',ylabel='price');
plt.savefig('gasolina.png')