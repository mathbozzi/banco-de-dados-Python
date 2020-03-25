import matplotlib.pyplot as plt 

x1 = [1,3,5,7,9]
y1 = [4,2,9,6,10]

x2 = [2,4,6,8,10]
y2 = [2,5,1,8,5]


eixox = "familias"
eixoy = "pessoas"
titulo = "População"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1,y1,label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()
plt.show()

# https://matplotlib.org/api/pyplot_summary.html
# https://matplotlib.org/api/index.html
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
