# Mailing_Partenariat_Gala
Service de mailing pour les responsable partenariat du gala d'IMT Mines alès


#Données

A partir d'un excel qui donne les information sur le contact, le département cible et l'entreprise. Le corps du texte est contenue dans les deux json, modifiable si besoin


# Utilisation

## Configuration
Deux confugration possibles 

  - configuration avec une adresse gmail
  
  - configuration avec une adresse de l'école
  
pour le moment : Faire la configuration au préalable : 

  pour gmail : il faut indiquer 'smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx)'
  
  pour mines : 'smtplib.SMTP_SSL("mail.mines-ales.org", port=465, context=ctx)'
  
 ## Utilisation
 
 Faire les instalation néssésaire (python 3.9+) et les librairies utiliser via le 'requirement.txt'
 
 lancer le fichier 'mailing.py' et se connecter à la boite mail (login + mdp)
  
 
