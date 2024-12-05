# coding: utf8
# chargement des fonctionnalité d'image ainsi que de low et high
from stegano import *
import os
dossier_resultat = 'resultat'
os.makedirs(dossier_resultat, exist_ok=True)

def decode(filename:str, filename_res:str, n:int):
    size, image = image_load(filename)
    result = image_new(size)
    for i in range(len(image)):
        low_bits = low(image[i], n)
        result[i] = low_bits << (8 - n)
    image_save(result, size, f'{dossier_resultat}/{filename_res}')

def encode(mask:str, filename:str, filename_res:str, n:int):
    size, image = image_load(filename)
    mask_size, mask = image_load(mask)
    result = image_new(size)

    for i in range(len(image)):
        high_bits_image = high(image[i], n)
        high_bits_mask = high(mask[i], n)
        result[i] = high_bits_mask + (high_bits_image >> n)

    image_save(result, size, f'{dossier_resultat}/{filename_res}')