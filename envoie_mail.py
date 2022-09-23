
import smtplib
import ssl
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

PASS_MINES  = ""

ctx = ssl.create_default_context()
password = PASS_MINES  # Your app password goes here
sender = "maxim.mangematin--mathey@mines-ales.org"    # Your e-mail address
receiver = ["maxim.mangematin@gmail.com"] # Recipient's address
# on crée un e-mail
message = MIMEMultipart("alternative")
# on ajoute un sujet
message["Subject"] = "Python test hehe"
# un émetteur
message["From"] = sender
# un destinataire
message["To"] = ', '.join(receiver)


html = '''
<html>
<body>
<h1>Salut salut {}</h1>
<p>C'est du bon python</p>
<b>Cdt</b>
<br>
<a href="https://galaminesales.fr/">mon_lien_incroyable du gala ! </a>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eget pretium ipsum. Sed dictum nibh feugiat dui aliquet congue. Ut porta nec metus vitae rhoncus. Maecenas ut tristique turpis. Praesent accumsan felis id dui dapibus varius. Nunc euismod justo vitae turpis cursus tempus. Morbi dapibus, dui interdum pulvinar sagittis, felis mauris porttitor lorem, vitae blandit risus nulla quis dolor. Aenean eu iaculis metus. Aenean neque mi, posuere in suscipit in, egestas vitae tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lobortis ante et dui condimentum, a consequat diam scelerisque. Duis ultrices dapibus est sed mattis.</p>
<p><img src="/content/Maxim.png"></p>'
</body>
</html>
'''
html_mime = MIMEText(html.format("nom de la boite"), 'html')
message.attach(html_mime)

convention = MIMEApplication(open("./data/Convention de partenariat - Gala 2022.pdf", "rb").read())
convention.add_header("Content-Disposition", "attachement", filename = "Convention de partenariat - Gala 2022.pdf" )
message.attach(convention)

dossier = MIMEApplication(open("./data/Dossier de partenariat - Gala 2022.pdf", "rb").read())
dossier.add_header("Content-Disposition", "attachement", filename = "Dossier de partenariat - Gala 2022.pdf" )
message.attach(dossier)




with smtplib.SMTP_SSL("mail.mines-ales.org", port=465, context=ctx) as server:
    server.login("maxim.mangematin--mathey", password)
    server.sendmail(sender, receiver, message.as_string())