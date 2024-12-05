# coding: utf8
# chargement des fonctionnalité d'image ainsi que de low et high
from stegano import *
import os
dossier_resultat = 'resultat'
os.makedirs(dossier_resultat, exist_ok=True)

def decode(filename:str):
    size, image = image_load(filename)
    result = image_new(size)
    for i in range(len(image)):
        low_bits = low(image[i], 4)
        result[i] = low_bits << (8 - 4)
    image_save(result, size, f'{dossier_resultat}/resultat_decode.png')

def encode(filename:str):
    size, image = image_load(filename)
    mask_size, mask = image_load('mask.jpg')
    result = image_new(size)

    for i in range(len(image)):
        high_bits_image = high(image[i], 4)
        high_bits_mask = high(mask[i], 4)
        result[i] = high_bits_mask + (high_bits_image >> 4)

    image_save(result, size, f'{dossier_resultat}/resultat_encode.png')