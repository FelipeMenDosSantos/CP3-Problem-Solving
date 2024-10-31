import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Funções para Custo, Receita e Lucro
def custo(x):
    return 120 * x**2 + 25 * x

def receita(x):
    return 60 * x

def lucro(x):
    return receita(x) - custo(x)

# Variando o número de unidades produzidas
x_values = np.arange(0, 100, 1)
lucro_values = lucro(x_values)

# Configuração do estilo do Seaborn
sns.set(style="whitegrid")

# Criando o gráfico para a evolução do lucro em função da produção
plt.figure(figsize=(12, 6))
sns.lineplot(x=x_values, y=lucro_values, color="red", linewidth=2.5, label="Lucro (L(x))")
plt.xlabel("Unidades Produzidas (x)")
plt.ylabel("Lucro")
plt.title("Evolução do Lucro em Função da Produção")
plt.legend()
plt.grid(True)
plt.show()
