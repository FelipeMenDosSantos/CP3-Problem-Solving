import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Definindo os fatores externos
taxa_imposto = 10  # em porcentagem sobre o lucro
aumento_materia_prima = 5  # em porcentagem de aumento no custo das matérias-primas

# Funções de Custo, Receita e Lucro ajustadas
def custo_ajustado(x):
    return (120 * x**2 + 25 * x) * (1 + aumento_materia_prima / 100)

def receita(x):
    return 60 * x

def lucro_ajustado(x):
    lucro_bruto = receita(x) - custo_ajustado(x)
    return lucro_bruto * (1 - taxa_imposto / 100)

# Variando o número de unidades produzidas
x_values = np.arange(0, 100, 1)
lucro_values = lucro_ajustado(x_values)

# Plotando o gráfico com as novas variáveis
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=x_values, y=lucro_values, color="purple", linewidth=2.5, label="Lucro Ajustado (L(x))")
plt.xlabel("Unidades Produzidas (x)")
plt.ylabel("Lucro Ajustado")
plt.title("Evolução do Lucro em Função da Produção com Fatores Externos")
plt.legend()
plt.grid(True)
plt.show()
