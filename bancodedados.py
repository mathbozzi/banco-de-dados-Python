import pymysql

host = "localhost"
user = "root"
password = ""
db = "filmes"
port = 3306

con = pymysql.connect(host, user, password, db, port)

c = con.cursor(pymysql.cursors.DictCursor)

arquivo = open("filmes - filmes.tsv").readlines()
for i in range(len(arquivo)):
    arquivo[i] = arquivo[i].replace("\n", "")
    arquivo[i] = arquivo[i].replace("'","")


class Filmes:
    id_aluno = "DEFAULT"
    filme = []
    genero = []
    nota_especialistas = []
    nota_audiencia = []
    custo = []
    ano = []

    # def __str__(self):
    #     return (self.id_aluno + "," + str(self.filme) + "," + str(self.genero)+"," + int(self.nota_especialistas)+","+int(self.nota_audiencia)+","+int(self.custo)+"," + str(self.ano))


filme = Filmes()

for i in range(len(arquivo)):
    if i != 0:
        linha = arquivo[i].split("\t")
        filme.filme.append((str(linha[0])))
        filme.genero.append(str(linha[1]))
        filme.nota_especialistas.append(int(linha[2]))
        filme.nota_audiencia.append(int(linha[3]))
        filme.custo.append(int(linha[4]))
        filme.ano.append(str(linha[5]))

# for i, filme in enumerate(filme.filme):
#     print(i,filme)


def insert(values, table, fields=None):  # funcao que insere uma classe no bd

    global c, con

    for i in range(len(values.filme)):
        query = "INSERT INTO " + table
        if(fields):
            query = query + " (" + fields + ") "
        query = query + " VALUES (" + str(values.id_aluno) + ",'" + values.filme[i]+"','" + values.genero[i]+"'," + str(values.nota_especialistas[i])+"," + str(values.nota_audiencia[i])+","+str(values.custo[i])+",'"+values.ano[i]+"')"

        c.execute(query)
        con.commit()

# insert(filme, "filme")

def select(fields, tables, where=None, desc_asc = None, delimitador=None ): 

    global c

    query = "SELECT " + fields + " FROM " + tables

    if(where):
        query = query + " ORDER BY " + where +" "+ desc_asc +" LIMIT " + delimitador

    c.execute(query)
    return c.fetchall()

# result = select("*","filme","nota_audiencia", "desc", "10") # 10 melhores filmes avaliados pela audiencia
# result = select("*","filme","nota_audiencia", "asc", "10") # 10 piores filmes avaliados pela audiencia
# result = select("*","filme","nota_especialistas", "asc", "10") # 10 piores filmes pelos especialistas
# result = select("*","filme","nota_especialistas", "desc", "10") # 10 melhores filmes pelos especialistas
# result = select("*","filme","custo", "desc", "1") # filme mais caro
# result = select("*","filme","custo", "asc", "1") # filme mais barato
# print(result)


def selectMax_Min(fields, tables, where=None, max_min = None): 

    global c

    query = "SELECT " + fields + " FROM " + tables

    if(where):
        query = query + " WHERE " + where +" = (SELECT "+ max_min+"("+where+") FROM " +tables+")"

    c.execute(query)
    return c.fetchall()

# result = selectMax_Min("*","filme","custo", "MAX") # retorna o filme mais caro
# result = selectMax_Min("*","filme","custo", "MIN") # retorna o filme mais barato
# print(result)

def selectMedia(value, table, where=None):
    
    global c

    query = "SELECT AVG("+value+") "
    if(where):
        query = query + "AS '"+where+"'"
    query = query +" FROM "+table

    c.execute(query)
    return c.fetchall()

# result = selectMedia("nota_especialistas","filme") #retorna a media das notas dos especialistas
# result = selectMedia("nota_audiencia","filme","media telespc") #retorna a media das notas dos telespectadores
# result = selectMedia("custo","filme","A media de custo(em milhoes):") #retorna a media do custo
# print(result)

def selectGeneros(value, table, where=None):
    global c

    query = "SELECT "+value+",COUNT("+value+") as 'total' FROM "+ table
    query = query + " GROUP BY "+value + " ORDER BY COUNT("+value+") desc LIMIT 10"

    print(query)
    c.execute(query)
    return c.fetchall()

result = selectGeneros("genero","filme")
print(len(result),result)


# SQL(EXEMPLOS PRATICOS ABAIXO  PARA BANCO DE DADOS)

# 1. Quais são os 10 filmes mais apreciados pelo público?
# select * from filmes order by nota_audiencia desc limit 10
 
# 2. Quais são os 10 filmes mais apreciados pela crítica especializada?
# select * from filmes order by nota_especialistas desc limit 10
 
# 3. Quais são os 10 filmes mais odiados pelo público?
# select * from filmes order by nota_audiencia limit 10
 
# 4. Quais são os 10 filmes mais odiados pela crítica especializada?
# select * from filmes order by nota_especialistas limit 10
 
 
# AULA 2
 
# 5. Qual filme com maior custo e qual filme com menor custo?
# # menor
# select * from filmes order by custo limit 1
# # maior
# select * from filmes order by custo limit 1
 
# SELECT * FROM filmes WHERE custo = (SELECT MAX(custo) FROM filmes )
 
# AULA 3
# 6. Qual a média da nota da crítica especializada?
# select avg(nota_especialistas) from filmes
 
# 7. Qual a média da nota do público?
# select avg(nota_audiencia) from filmes
 
# 8. Qual a média de custo de filmes?
# select avg(custo) from filmes
 
# AULA 4
# 9. Quantos filmes custaram mais do que o custo médio de filmes da tabela?
# select count(*) from filmes where custo > (select avg(custo) from filmes)
 
# 10. Quais são os filmes com nota acima da média da nota dada pela crítica especializada?
# select * from filmes where nota_especialistas > (select avg(nota_especialistas) from filmes)
 
# 11. Quais são os filmes com nota acima da média da nota dada pelo público? Quais os melhores?
# select * from filmes where nota_audiencia > (select avg(nota_audiencia) from filmes) order by nota_audiencia desc
 
# AULA 5
# 12. Quais são os tipos de categoria existentes?
# select genero from filmes group by genero
 
# 13. Quais são os gêneros com maior quantidade de filmes?
# select count(genero) as total, genero from filmes group by genero order by total desc
 
# AULA 6
# 14. Qual gênero tem a mais alta média de custo?
# select avg(custo) as 'Thriller' from filmes where genero = 'Thriller';
# select avg(custo) as 'Comedy' from filmes where genero = 'Comedy';
# select avg(custo) as 'Romance' from filmes where genero = 'Romance';
# select avg(custo) as 'Drama' from filmes where genero = 'Drama';
# select avg(custo) as 'Horror' from filmes where genero = 'Horror';
# select avg(custo) as 'Action' from filmes where genero = 'Action';
# select avg(custo) as 'Adventure' from filmes where genero = 'Adventure';
# AULA 7
# 15. Qual gênero tem a mais alta média de nota para o público?
# select avg(nota_audiencia) as 'Thriller' from filmes where genero = 'Thriller';
# select avg(nota_audiencia) as 'Comedy' from filmes where genero = 'Comedy';
# select avg(nota_audiencia) as 'Romance' from filmes where genero = 'Romance';
# select avg(nota_audiencia) as 'Drama' from filmes where genero = 'Drama';
# select avg(nota_audiencia) as 'Horror' from filmes where genero = 'Horror';
# select avg(nota_audiencia) as 'Action' from filmes where genero = 'Action';
# select avg(nota_audiencia) as 'Adventure' from filmes where genero = 'Adventure';
 
# 16. Qual gênero tem a mais alta média de nota para a crítica especializada?
# select avg(nota_especialistas) as 'Thriller' from filmes where genero = 'Thriller';
# select avg(nota_especialistas) as 'Comedy' from filmes where genero = 'Comedy';
# select avg(nota_especialistas) as 'Romance' from filmes where genero = 'Romance';
# select avg(nota_especialistas) as 'Drama' from filmes where genero = 'Drama';
# select avg(nota_especialistas) as 'Horror' from filmes where genero = 'Horror';
# select avg(nota_especialistas) as 'Action' from filmes where genero = 'Action';
# select avg(nota_especialistas) as 'Adventure' from filmes where genero = 'Adventure';
 
# AULA 8
# 17. Quantos filmes foram produzidos por ano?
# select count(ano), ano from filmes group by ano
 
# 18. Qual ano produziu mais filmes?
# select count(ano) as total, ano from filmes group by ano order by total desc
 
# AULA 9
# 19. Qual genêro produziu mais filmes em um ano?
# select count(ano) as total, ano, GENERO from filmes group by ano, genero order by total desc
 
# 20. Qual o filme mais amado pela audiência e pelos especialistas ao mesmo tempo?
# select filme, (nota_audiencia+nota_especialistas)/2 as a from filmes order by a desc;