import cProfile
from dis import show_code
from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from msilib.schema import ComboBox
from multiprocessing.reduction import send_handle
from pickle import FALSE
import smtplib
from PyQt5 import uic,QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
import icones.icons as icons
import mysql.connector
import re
import webbrowser
import random
import Envio_Email.enviaremail as enviaremail
import icones.pordutosicons as pordutosicons

def acessar_email():
    new=2
    url="https://www.gmail.com/"

    webbrowser.open(url,new=new)

def logar():

    projetoo.frame_2.close()
    
    
def voltar_logar():
    projetoo.frame_2.show()
def registrar():
    

    
    global codigo
    global masculino
    global nome
    global cpf
    global email
    nome = projetoo.lineEdit.text()
    senha= projetoo.lineEdit_2.text()
    cpf = projetoo.lineEdit_3.text()
    email = projetoo.lineEdit_4.text()
    codigo = projetoo.lineEdit_5.text()
    masculino = projetoo.radioButton.text()
    feminino = projetoo.radioButton_2.text()
    outtro = projetoo.radioButton_3.text()
    if nome == "" or senha == "" or cpf == "" or email == "" or codigo == "" or projetoo.radioButton.isChecked() == False and   projetoo.radioButton_2.isChecked() == False and  projetoo.radioButton_3.isChecked() == False:
        QMessageBox.warning(projetoo, "Aviso", "PREENCHA TODOS OS CAMPOS")
    else:
        validar_nome = (re.findall(r'^[a-zA-Z]{1,}',nome))
        validar_cpf = (re.findall(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',cpf))
        if validar_cpf == []:
             QMessageBox.warning(projetoo, "Aviso", " CPF INVALIDO")
        else:
            if validar_nome == []:
                QMessageBox.warning(projetoo, "AVISO", "Insira um valor de nome valido")
            else:
                try:
                    sql = f"Select nome from Pessoas where nome = '{nome}'"
                    con = mysql.connector.connect(host = "localhost", user="root", password="sirlei231",database="banco")
                    cursor = con.cursor()
                    cursor.execute(sql)
                    dado_nome = cursor.fetchall()
                    con.close()
                    cursor.close()
                    if len(dado_nome) !=0:
                        QMessageBox.warning(projetoo,"AVISO", "ESSE NOME JA FOI CADASTRO, TENTE OUTRO")
                    else:
                        validador_senha = (re.findall(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\u0020-\u002f-\u003A-\u0040\-\u005B-\u0060-\u007B-\u007E]).{8}',senha))
                        if validador_senha == []:
                            QMessageBox.warning(projetoo,"Aviso","senha invalida, verifique se a sua senha atende aos requisitos: ter 8 caracteres, contendo numero, letra maiscula e caracter especial")
                        else:
                            if "gmail" not in email:
                                QMessageBox.warning(projetoo, "AVISO", "INFORME UM GMAIL VALIDO")
                            else:
                                if projetoo.radioButton.isChecked():
                                    sql2 = f"Insert Into Pessoas (id,nome,sexo,cpf,senha,gmail) values ('{codigo}','{nome}','M','{cpf}','{senha}','{email}')"
                                    con2 = mysql.connector.connect(host = "localhost", user="root",password="sirlei231", database="banco")
                                    cursor2 = con2.cursor()
                                    cursor2.execute(sql2)
                                    con2.commit()
                                    con2.close()
                                    cursor2.close()  
                                    QMessageBox.about(projetoo,"AVISO", "REGISTRO REALIZADO COM SUCESSO")
                                    limpar() 
                                    projetoo.close()
                                    produto.show()
                                    sql = "Select * From Produto"
                                    con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database= "banco")
                                    cursor = con.cursor()
                                    cursor.execute(sql)
                                    dados = cursor.fetchall()
                                    cursor.close()
                                    con.close()
                                    produto.tableWidget.setRowCount(len(dados))
                                    produto.tableWidget.setColumnCount(7)
                                    for c in range(len(dados)):
                                        for i in range(0, 7):
                                            produto.tableWidget.setItem(c,i, QtWidgets.QTableWidgetItem(str(dados[c][i])))
                                if projetoo.radioButton_2.isChecked():
                                    sql2 = f"Insert Into Pessoas (id,nome,sexo,cpf,senha,gmail) values ('{codigo}','{nome}','F','{cpf}','{senha}','{email}')"
                                    con2 = mysql.connector.connect(host = "localhost", user="root",password="sirlei231", database="banco")
                                    cursor2 = con2.cursor()
                                    cursor2.execute(sql2)
                                    con2.commit()
                                    con2.close()
                                    cursor2.close()  
                                    QMessageBox.about(projetoo,"AVISO", "REGISTRO REALIZADO COM SUCESSO") 
                                    limpar()
                                    projetoo.close()
                                    produto.show()
                                    sql = "Select * from Produto"
                                    con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "banco" )
                                    cursor = con.cursor()
                                    cursor.execute(sql)
                                    dados = cursor.fetchall()
                                    con.close()
                                    cursor.close()
                                    produto.tableWidget.setRowCount(len(dados))
                                    produto.tableWidget.setColumnCount(7)
                                    for c in range (len(dados)):
                                        for i in range(0, 7):
                                            produto.tableWidget.setItem(c, i, QtWidgets.QTableWidgetItem(str(dados[c][i])))
                                if projetoo.radioButton_3.isChecked():
                                    sql2 = f"Insert Into Pessoas (id,nome,sexo,cpf,senha,gmail) values ('{codigo}','{nome}','O','{cpf}','{senha}','{email}')"
                                    con2 = mysql.connector.connect(host = "localhost", user="root",password="sirlei231", database="banco")     
                                    cursor2 = con2.cursor()
                                    cursor2.execute(sql2)
                                    con2.commit()
                                    con2.close()
                                    cursor2.close()
                                    QMessageBox.about(projetoo,"AVISO", "REGISTRO REALIZADO COM SUCESSO")
                                    limpar()
                                    projetoo.close()
                                    produto.show()
                                    sql = "Select * From Produto"
                                    con = mysql.connector.connect(host = "localhost", user= "root", password = "sirlei231", database = "banco" )
                                    cursor = con.cursor()
                                    cursor.execute(sql)
                                    dados = cursor.fetchall()
                                    print(dados)
                                    con.close()
                                    cursor.close()
                                    produto.tableWidget.setRowCount(len(dados))
                                    produto.tableWidget.setColumnCount(7)
                                    for c in range(len(dados)):
                                        for i in range(0,7):
                                            produto.tableWidget.setItem(c,i, QtWidgets.QTableWidgetItem(str(dados[c][i])))
            
                                
                except mysql.connector.errors.IntegrityError:
                    QMessageBox.warning(projetoo,"AVISO","o codigo informado ja foi cadastrado ")
                
def Login():
    nome_login = projetoo.lineEdit_6.text()
    senha_login = projetoo.lineEdit_7.text()
    sql = f"Select nome From Pessoas where nome =  '{nome_login}'"
    con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "banco")
    cursor = con.cursor()
    cursor.execute(sql)
    dados3 = cursor.fetchall()
    cursor.close()
    con.close()
    if len(dados3) == 0 :
        QMessageBox.warning(projetoo, "Aviso", "Nome não cadastrado") 
    else:
        sql = f"Select senha from Pessoas where nome = '{nome_login}'"
        con = mysql.connector.connect(host= "localhost", password = "sirlei231", user = "root", database = "banco")
        cursor = con.cursor()
        cursor.execute(sql)
        dados4 = cursor.fetchall()
        cursor.close()
        con.close()
        if dados4[0][0] != senha_login:
            QMessageBox.warning(projetoo,"Aviso","Senha incorreta" )
        else:
            sql = f"Select id from Pessoas where nome = '{nome_login}'"
            con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database= "banco")
            cursor = con.cursor()
            cursor.execute(sql)
            codigo = cursor.fetchall()
            cursor.close()
            con.close()
            QMessageBox.about(projetoo,"Aviso","Logado Com Sucesso")
            print(codigo[0][0])
            projetoo.close()
            produto.show()
            comandomysql = "Select * from Produto"
            con = mysql.connector.connect(host = "localhost", password = "sirlei231",database = "banco",user ="root")
            cursor = con.cursor()
            cursor.execute(comandomysql)
            dados = cursor.fetchall()
            cursor.close()
            con.close()
            produto.tableWidget.setRowCount(len(dados))
            produto.tableWidget.setColumnCount(7)
            #primeiro for pega a linha de registro do banco, segundo for pega cada coluna, ex: o primeiro for começa em 0 referente a primeira linha então entra no segundo referente a cada coluna onde cada dado da linha 0 sera adicionado ficando: [0][0] primeiro item da primeira coluna [0][1] primeiro item da segunda coluna.... o comando setItem sera responsavel por mostra na table widget a listagem, resumindo: primeiro for 0, [0][1],[0][2],[0][3] ou seja todos os primeiros itens de cada coluna
            
            for c in range (len(dados)):
                for i in range(0, 7):
                   produto.tableWidget.setItem(c,i, QtWidgets.QTableWidgetItem(str(dados[c][i])))



    

def limpar():
    projetoo.lineEdit.clear()     
    projetoo.lineEdit_2.clear()
    projetoo.lineEdit_3.clear()
    projetoo.lineEdit_4.clear()
    projetoo.lineEdit_5.clear()

def esqueceu_senha():
    projetoo.frame_3.hide()
    projetoo.frame_5.hide()
    projetoo.frame_4.show()
def voltar_logar2():
    projetoo.frame_3.show()
def resetar_senha():
    global nome_loginn
    nome_loginn = projetoo.lineEdit_8.text()
    global senha_nova
    senha_nova = projetoo.lineEdit_9.text()
    sql = f"Select nome from Pessoas where nome = '{nome_loginn}'"
    con = mysql.connector.connect(host = "localhost", user= "root", password = "123456", database= "banco")
    cursor = con.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()
    cursor.close()
    con.close()
    if len(dados) == 0:
        QMessageBox.warning(projetoo,"Aviso", "o nome não foi cadastrado")
    else:
        validar =  (re.findall(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\u0020-\u002f-\u003A-\u0040\-\u005B-\u0060-\u007B-\u007E]).{8}',senha_nova))
        if validar == []:
            QMessageBox.warning(projetoo,"Aviso","Senha Nova Invalida verifique se a sua senha atende aos requisitos: ter 8 caracteres, contendo numero, letra maiscula e caracter especial")
        else:   
                sql = f"Select gmail from Pessoas where nome = '{nome_loginn}'"
                con = mysql.connector.connect(host = "localhost", user= "root", password = "123456", database= "banco")
                cursor = con.cursor()
                cursor.execute(sql)
                dadoss = cursor.fetchall()
                cursor.close()
                con.close()
                global codigo_reset
                codigo_reset = str(random.randint(100, 999))
                enviaremail.enviarr_email(dadoss, codigo_reset)
                projetoo.lineEdit_8.clear()
                projetoo.lineEdit_9.clear()
                projetoo.frame_5.show()

def codigo_email():
   codigo_resetar = projetoo.lineEdit_10.text()
   if codigo_resetar != codigo_reset:
       QMessageBox.warning(projetoo,"aviso","codigo invalido")
   else:
        sql = f"update Pessoas set senha ='{senha_nova}' where nome = '{nome_loginn}'"
        con = mysql.connector.connect(host = "localhost", user= "root", password = "123456", database= "banco")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        cursor.close()
        QMessageBox.about(projetoo,"aviso","senha alterada com sucesso")
        projetoo.lineEdit_10.clear()
        projetoo.frame_3.show()

def adicionar():
    nome_produto = produto.lineEdit.text()
    descricao_produto = produto.lineEdit_4.text()
    preço = produto.doubleSpinBox.value()
    categoria = produto.comboBox.currentText()
    data = produto.dateEdit.date().toPyDate()
    quantia = produto.spinBox.value()
    unidade = produto.comboBox_2.currentText()
    validar_nome_produto = re.findall(r'[a-zA-Z]{1,}', nome_produto)
    
    if validar_nome_produto == []:
        QMessageBox.warning(produto, "aviso", "nome de produto invalido")
    else:
        validar_descricao_produto = re.findall(r'[a-zA-Z]{1,}', descricao_produto)
        if validar_descricao_produto == []:
            QMessageBox.warning(produto, "aviso", "descriçao invalida")
        else:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "banco")
            sql = f"Insert Into Produto(nome, preço, quantia, descricao, data_compra, unidade) values ('{nome_produto}','{preço}','{quantia}','{descricao_produto}','{data}', '{unidade}')"
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            con.close()
            cursor.close()
            QMessageBox.about(produto, "aviso", "produto cadastrado com sucesso")
            produto.lineEdit.clear()
            produto.lineEdit_4.clear()

            comandomysql = "Select * from Produto"
            con = mysql.connector.connect(host = "localhost", password = "sirlei231",database = "banco",user ="root")
            cursor = con.cursor()
            cursor.execute(comandomysql)
            dados = cursor.fetchall()
            cursor.close()
            con.close()
            produto.tableWidget.setRowCount(len(dados))
            produto.tableWidget.setColumnCount(7)
            for c in range (len(dados)):
                for i in range(0, 7):
                   produto.tableWidget.setItem(c,i, QtWidgets.QTableWidgetItem(str(dados[c][i])))

def deletar():
    linha = produto.tableWidget.currentRow() #pegando linha selecionada
    sql2 = "Select id from Produto"
    con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "banco")
    cursor = con.cursor()
    cursor.execute(sql2)
    ids = cursor.fetchall()#retorna uma tupla com todos os ids
    con.close()
    cursor.close()
    id_da_linha = ids[linha][0] #ex:ids[1][0]: id da coluna 1, 1 = linha selecionada, 0 = coluna referente ao id, e ids é a tupla de ids no banco
    produto.tableWidget.removeRow(linha) #removendo linha da tabela
    sql = f"Delete From Produto where id = {id_da_linha}"
    con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "banco")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

def atualizar():
    nome_produtoo = produto.lineEdit.text()
    descricao_produtoo = produto.lineEdit_4.text()
    preçoo = produto.doubleSpinBox.value()
    categoria = produto.comboBox.currentText()
    dataa = produto.dateEdit.date().toPyDate()
    quantiaa = produto.spinBox.value()
    unidade = produto.comboBox_2.currentText()
    linha = produto.tableWidget.currentRow()
    sql = "select id from Produto"
    con = mysql.connector.connect(host="localhost", user = "root", password = "sirlei231", database = "banco")
    cursor = con.cursor()
    cursor.execute(sql)
    ids = cursor.fetchall()
    con.close()
    cursor.close()
    id_produto = ids[linha][0]
    sql5 = f"Update Produto set nome = '{nome_produtoo}', preço = '{preçoo}', quantia='{quantiaa}', descricao = '{descricao_produtoo}', data_compra = '{dataa}', unidade='{unidade}' where id = {id_produto}"
    con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "banco")
    cursor = con.cursor()
    cursor.execute(sql5)
    con.commit()
    con.close()
    cursor.close()
    sql6 = f"select * from Produto where id = {id_produto}"
    con = mysql.connector.connect(host = "localhost", user = "root", password="sirlei231", database="banco") 
    cursor = con.cursor()
    cursor.execute(sql6)
    dados = cursor.fetchall()
    con.close()
    cursor.close()
    #adicionando os dados na tabela
    for c in range(len(dados)):
        for i in range(0, 7): #colunas
            produto.tableWidget.setItem(c,i,QtWidgets.QTableWidgetItem(str(dados[c][i])))   


app = QtWidgets.QApplication([])
projetoo = uic.loadUi("projetoo.ui")
produto = uic.loadUi("tela_produto.ui")
projetoo.setWindowTitle("Cadastro")
projetoo.setWindowIcon(QtGui.QIcon("logo.png"))
projetoo.pushButton.clicked.connect(registrar)
projetoo.pushButton_2.clicked.connect(logar)
projetoo.pushButton_5.clicked.connect(voltar_logar)
projetoo.pushButton_3.clicked.connect(Login)
projetoo.pushButton_6.clicked.connect(acessar_email)
projetoo.pushButton_4.clicked.connect(esqueceu_senha)
projetoo.pushButton_8.clicked.connect(voltar_logar2)
projetoo.pushButton_7.clicked.connect(resetar_senha)
projetoo.pushButton_9.clicked.connect(codigo_email)
produto.adicionarrr.clicked.connect(adicionar)
produto.pushButton_2.clicked.connect(deletar)
produto.pushButton_3.clicked.connect(atualizar)


projetoo.show()
app.exec()