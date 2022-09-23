
import smtplib
import ssl
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email.mime.image import MIMEImage


USERNAME = str(input("Login mail mines : "))
PASS_MINES  = str(input("password mail mines : "))

ctx = ssl.create_default_context()
password = PASS_MINES  # Your app password goes here
sender = "{}@mines-ales.org".format(USERNAME)    # Your e-mail address
# on crée un e-mail


with open("./data/corps.txt", "r", encoding="utf-8") as source_corps:
    corps = source_corps.read()


def generate_mail(nom_entreprise, dpt, contact):
    
    message = MIMEMultipart("alternative")
    
    # on ajoute un sujet
    message["Subject"] = "Demande de partenariat {}".format(nom_entreprise)
    # un émetteur
    message["From"] = sender
    # un destinataire
    message["To"] = contact

    current_body = corps.replace("Nom_entreprise", nom_entreprise).replace("Nom_envoyeur", " ".join(USERNAME.split(".")))

    current_body = current_body.replace("\n", "<br>")


    html = '''
    <html>
    <body>
    <h1>Salut salut {}</h1>
    <p>C'est du bon python</p>
    <b>Cdt</b>
    <br>
    <p>{}</p>
    <p><<img src="cid:sign">></p>'
    </body>
    </html>
    '''
    html_mime = MIMEText(html.format(nom_entreprise, current_body), 'html')
    message.attach(html_mime)

    #attachement
    convention = MIMEApplication(open("./data/Convention de partenariat - Gala 2022.pdf", "rb").read())
    convention.add_header("Content-Disposition", "attachement", filename = "Convention de partenariat - Gala 2022.pdf" )
    message.attach(convention)

    dossier = MIMEApplication(open("./data/Dossier de partenariat - Gala 2022.pdf", "rb").read())
    dossier.add_header("Content-Disposition", "attachement", filename = "Dossier de partenariat - Gala 2022.pdf" )
    message.attach(dossier)

    #signature
    with open('./data/signature.png', 'rb') as sig:
        signature = MIMEImage(sig.read())
    signature.add_header('Content-ID', '<sign>')
    message.attach(signature)

    return contact, message


def send_mail(message, receiver):
    with smtplib.SMTP_SSL("mail.mines-ales.org", port=465, context=ctx) as server:
        server.login(USERNAME, password)
        server.sendmail(sender, receiver, message.as_string())

contact, msg =  generate_mail("gala", "2IA", "maxim.mangematin@gmail.com")
send_mail(msg, contact)