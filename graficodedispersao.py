import matplotlib.pyplot as plt 

x1 = [1,3,5,7,9]
y1 = [4,2,9,6,10]

x2 = [2,4,6,8,10]
y2 = [2,5,1,8,5]


eixox = "x"
eixoy = "y"
titulo = "Grafico de dispersão"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1,y1, label = "Meus pontos",color = "orange") #pontos
plt.plot(x1,y1,color = "#990000",linestyle = "--") #linhas
# plt.show()
plt.savefig("figura1.png")
plt.savefig("figura1.pdf")
plt.savefig("figura.png",dpi = 300) #quanto maior dpi maior a resolução




# https://matplotlib.org/api/pyplot_summary.html
# https://matplotlib.org/api/index.html
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
