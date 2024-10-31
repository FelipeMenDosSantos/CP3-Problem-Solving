import numpy as np
import matplotlib.pyplot as plt

# Funções para Custo, Receita e Lucro
def custo(x):
    return 120 * x**2 + 25 * x

def receita(x):
    return 60 * x

def lucro(x):
    return receita(x) - custo(x)

# Variando o número de unidades produzidas
x_values = np.arange(0, 100, 1)
custo_values = custo(x_values)
receita_values = receita(x_values)
lucro_values = lucro(x_values)

# Plotando os resultados
plt.figure(figsize=(12, 6))
plt.plot(x_values, custo_values, label="Custo (C(x))", color="blue")
plt.plot(x_values, receita_values, label="Receita (R(x))", color="green")
plt.plot(x_values, lucro_values, label="Lucro (L(x))", color="red")
plt.xlabel("Unidades Produzidas (x)")
plt.ylabel("Valor")
plt.title("Variação de Custo, Receita e Lucro com o Número de Unidades Produzidas")
plt.legend()
plt.grid(True)
plt.show()