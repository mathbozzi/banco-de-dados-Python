
import matplotlib.pyplot as plt 
import random

vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0,100)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.show()