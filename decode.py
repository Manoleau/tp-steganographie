# coding: utf8
# chargement des fonctionnalité d'image ainsi que de low et high
from stegano import *
import os
dossier_resultat = 'resultat'
os.makedirs(dossier_resultat, exist_ok=True)
# charge le fichier
size, image = image_load('message_x.png')

# crée une nouvelle image de résultat
result = image_new(size)

# ici votre code de décodage
...

# sauvegarde l'image
image_save(result, size, f'{dossier_resultat}/resultat.png')
