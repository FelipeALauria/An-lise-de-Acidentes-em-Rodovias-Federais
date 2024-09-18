import pandas as pd
import numpy as np
from scipy.stats import binom, chi2_contingency
import matplotlib.pyplot as plt


ds = pd.read_excel("C:\\Users\\felip\\Desktop\\Facul\\2024\\2 Semestre\\Probabilidade e Estatística\\Trabalho 2\\DadosEstradasBrasileiras.xlsx")

total_acidentes = 292659

sucessos_reais = ((ds['mortos'] == 0) & (ds['feridos'] == 0) & (ds['feridos_leves'] == 0) & (ds['feridos_graves'] == 0)).sum()

fracassos_reais = total_acidentes - sucessos_reais

p_sucesso_real = sucessos_reais / total_acidentes
p_fracasso_real = fracassos_reais / total_acidentes

print(f"Probabilidade de Sucesso Real (sem mortes): {p_sucesso_real:.2f}")
print(f"Probabilidade de Fracasso Real (com mortes): {p_fracasso_real:.2f}")
print('\n')
#Fim da analise dos dados reais.


n_simulacoes = 58532
simulacao_sucessos = binom.rvs(n=1, p=p_sucesso_real, size=n_simulacoes)

sucessos_simulados = np.sum(simulacao_sucessos == 1)
fracassos_simulados = n_simulacoes - sucessos_simulados

print(f"Sucessos Simulados (sem mortes): {sucessos_simulados}")
print(f"Fracassos Simulados (com mortes): {fracassos_simulados}")

print('\n')

print(f"Sucessos Simulados (sem mortes): {(sucessos_simulados/n_simulacoes):.2f}")
print(f"Fracassos Simulados (com mortes): {(fracassos_simulados/n_simulacoes):.2f}")
print('\n')
#Fim da simulação de novos dados com base nos dados reais.


observados = [sucessos_reais, fracassos_reais]
simulados = [sucessos_simulados, fracassos_simulados]

chi2, p_valor, _, _ = chi2_contingency([observados, simulados])

print(f"Valor de Qui-Quadrado: {chi2:.4f}")
print(f"P-valor: {p_valor:.4f}")

print('\n')
if p_valor > 0.05:
    print("Não há diferença estatisticamente significativa entre os dados reais e simulados (p > 0.05).")
else:
    print("Há uma diferença estatisticamente significativa entre os dados reais e simulados (p <= 0.05).")

labels = ['Sucesso (sem mortes)', 'Fracasso (com mortes)']
observed_counts = [sucessos_reais, fracassos_reais]
simulated_counts = [sucessos_simulados, fracassos_simulados]

x = np.arange(len(labels)) 

fig, ax = plt.subplots()
ax.bar(x - 0.2, observed_counts, 0.4, label='Reais')
ax.bar(x + 0.2, simulated_counts, 0.4, label='Simulados')

ax.set_xlabel('Eventos')
ax.set_ylabel('Contagem')
ax.set_title('Comparação de Sucessos e Fracassos (Reais vs Simulados)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()