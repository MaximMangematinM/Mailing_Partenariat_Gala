
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import json


USERNAME = str(input("Login mail mines : "))
PASS_MINES  = str(input("password mail mines : "))

ctx = ssl.create_default_context()
password = PASS_MINES  # Your app password goes here
sender = "{}@mines-ales.org".format(USERNAME)    # Your e-mail address


with open("./data/corps.txt", "r", encoding="utf-8") as source_corps:
    corps = source_corps.read()

with open("./data/forum.json", "r", encoding="utf-8") as f:
    forum_corps = json.load(f)

with open("./data/text_dpt.json", "r", encoding="utf-8") as f:
    dtp_corps = json.load(f)


def generate_mail(nom_entreprise : str, dpt : str, forum : str, contact : str, corps : str = corps) -> MIMEMultipart:
    
    message = MIMEMultipart("alternative")
    
    # on ajoute un sujet
    message["Subject"] = "Demande de partenariat {}".format(nom_entreprise)
    # un émetteur
    message["From"] = sender
    # un destinataire
    message["To"] = contact

    dpts = dpt.replace(" ", "").split(",")

    corps_dep = ""
    for dep in dpts:
        corps_dep = corps_dep + " " + dtp_corps[dep.upper()]


    corps = corps.format(forum_corps[forum.lower()], corps_dep)

    current_body = corps.replace("Nom_entreprise", nom_entreprise).replace("Nom_envoyeur", USERNAME.replace(".", " ")).replace("Nom_département", dpt)

    current_body = current_body.replace("\n", "<br>")

    html = '''
    <html>
    <body>
    <p>{}</p>
    <p><<img src="cid:sign">></p>'
    </body>
    </html>
    '''
    html_mime = MIMEText(html.format(current_body), 'html')
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

    return message


def send_mail(message : MIMEMultipart, receiver : str):
    with smtplib.SMTP_SSL("mail.mines-ales.org", port=465, context=ctx) as server:
        server.login(USERNAME, password)
        server.sendmail(sender, receiver, message.as_string())
