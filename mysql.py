import pymysql

host = "localhost"
user = "aplicacao"
password = "Matheusb#1"
db = "escola_curso"
port = 3306

con = pymysql.connect(host, user, password, db, port)

c = con.cursor(pymysql.cursors.DictCursor)


def select(fields, tables, where=None):  # funcao que retorta a lista do bd

    global c

    query = "SELECT " + fields + " FROM " + tables

    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()

#result = select("nome,endereco","alunos")

# print(result)


def insert(values, table, fields=None):  # funcao que insere uma lista no bd

    global c, con

    query = "INSERT INTO " + table

    if(fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()


values = [
    "DEFAULT,'VINICIUS BOZZI','2000-01-01','Av daS palmas','vitoria','es','12345678910'",
    "DEFAULT,'FABRICIO BOZZI','1980-01-01','Av daS PALMEIRAS','LISBOA','PO','34545678910'"]


# insert(values,"alunos")
# select("*","alunos")

def update(sets, table, where=None):  # funcao que atualiza dados de uma lista no bd

    global c, con

    query = "UPDATE " + table + " SET " + \
        ','.join([field + " = '" + value + "' " for field, value in sets.items()])
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    con.commit()

# update({"nome":"VINICIUS BOZZI","cidade":"VENDA NOVA","data_nascimento":"1996-08-22","estado":"ES","cpf":"65432109877"}, "alunos", "nome = 'Vinicius Bozzi'")
# print(select("*","alunos","nome = 'vinicius bozzi'"))


def delete(table, where):

    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()


# delete("alunos","nome = 'VINICIUS BOZZI'")
print(select("*", "alunos"))
