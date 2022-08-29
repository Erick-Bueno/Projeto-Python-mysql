import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
 
 
def enviarr_email(dados, codigao):
    host = "smtp.gmail.com"
    port = "587"
    login = "erickjb93@gmail.com"
    senha = "zrzhokxrkyzslcgd"

    servidor = smtplib.SMTP(host, port)
    servidor.ehlo()
    servidor.starttls()
    servidor.login(login, senha)

    messagem_email = MIMEMultipart()
    messagem_email["From"] = login
    messagem_email["To"] = dados[0][0]
    messagem_email["Subject"]="codigo de alteração de senha"  
    corpo = f"seu codigo é {codigao}"

    messagem_email.attach(MIMEText(corpo,"plain"))
    servidor.sendmail(messagem_email["From"], messagem_email["To"], messagem_email.as_string())
    servidor.quit()

               