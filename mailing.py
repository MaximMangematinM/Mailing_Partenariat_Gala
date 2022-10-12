import pandas as pd
import envoie_mail
import smtplib


donnees_contact = pd.read_excel("./data/crash_test.xlsx")

n = len(donnees_contact)

print(donnees_contact.head())


for i in range(n):
    line = donnees_contact.iloc[i]
    entreprise = line["Entreprise"]
    forum = line["Forum des entreprises"]
    dpts = line["Public cible"]
    mail = line["Contact"]

    msg = envoie_mail.generate_mail(nom_entreprise=entreprise, dpt=dpts, forum=forum, contact=mail)
    try:
        envoie_mail.send_mail(message=msg, receiver=mail)
    except smtplib.SMTPRecipientsRefused :
        print("Envoie immposible à {}".format(mail))

    print("Mail envoyé pour {} à {}".format(entreprise, mail))