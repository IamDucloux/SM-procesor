#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:25:15 2020

@author: ian

Procesador de notas de texto.
"""
#CONFIGURACION DE LIBRERIAS
import spacy
nlp = spacy.load("es_core_news_sm")
#FIN LIBCONFIG

# =============================================================================
# #CREAR ARCHIVO DE TEXTO
# f = open('texto.txt','wb')
# f.write('Si puedes leer esto el archivo de texto se genero')
# f.close
# =============================================================================

# =============================================================================
# #ESCRIBIR EN ARCHIVO CREADO
# f=open('texto.txt','a')
# f.write('\nMensaje')
# f.close
# =============================================================================

# =============================================================================
# #LEER ARCHIVO DE TEXTO
# f=open('texto.txt','r')
# mensaje = f.read()
# print(mensaje)
# f.close
# =============================================================================

f=open('texto.txt','r')
text=f.read()
print(text)
f.close

doc = nlp(text)

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
    
    



