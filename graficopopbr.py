import matplotlib.pyplot as plt 

arquivo = open("original.csv").readlines()

x = []
y = []

for i in range(len(arquivo)):
    if i != 0:
        linha = arquivo[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x,y, color = "#e4e4e4")
plt.plot(x,y, color ="k", linestyle = "--")
plt.title("Crescimento populacional do Brasil")
plt.xlabel("Ano")
plt.ylabel("Pessoas")
# plt.show()
plt.savefig("populacaobr.png", dpi = 300)
