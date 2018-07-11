#!/usr/bin/python3

import psycopg2 # --Conecta com o banco postgresql
try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux port=5432')
    cur = con.cursor()
    # cur.execute("insert into pessoas(nome, email, idade, telefone) values('mariazinha',\
    # 'mariazinha@teste.com',50,'978946122')")
    cur.execute('select * from pessoas')

    conteudo = cur.fetchall() # vai trazer todo o registro do select inserido.
  
    print(conteudo) #fetchone vai trazer só um registro

    # fetchall fetchone
    if con == 'Conectado com sucesso!':
        print('Conectado com sucesso!')
    else:
        cur = con.cursor()

    con.commit() #comita os inserts 
    cur.close() # fechar o cursor
    con.close() # fechar a conexao
except Exception as e:
    # cur.rollback() # se a conexao falhar, nada vai ser feito.
    print('Erro de conexao: {}'.format(e))







