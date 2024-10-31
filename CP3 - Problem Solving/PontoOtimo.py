import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import fmin

# Funções de Custo, Receita e Lucro
def custo(x):
    return 120 * x**2 + 25 * x

def receita(x):
    return 60 * x

def lucro(x):
    return receita(x) - custo(x)

# Função negativa do lucro para maximizar usando fmin
def lucro_neg(x):
    return -lucro(x)

# Encontrando o ponto ótimo
x_otimo = fmin(lucro_neg, x0=1, disp=False)[0]
lucro_otimo = lucro(x_otimo)

# Variando o número de unidades produzidas
x_values = np.arange(0, 100, 1)
lucro_values = lucro(x_values)

# Plotando o gráfico com o ponto ótimo
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=x_values, y=lucro_values, color="red", linewidth=2.5, label="Lucro (L(x))")
plt.scatter(x_otimo, lucro_otimo, color="blue", s=100, label=f'Ponto Ótimo (x={x_otimo:.2f}, L={lucro_otimo:.2f})')
plt.xlabel("Unidades Produzidas (x)")
plt.ylabel("Lucro")
plt.title("Evolução do Lucro em Função da Produção com Ponto Ótimo")
plt.legend()
plt.grid(True)
plt.show()
