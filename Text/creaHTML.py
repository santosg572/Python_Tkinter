#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys

def doc(file='', titulo=''):
  fil = open(file, 'w')
  fil.write('<!DOCTYPE html>\n')
  fil.write('<html>\n')
  fil.write('<head>\n')
  fil.write('<title>Page Title</title>\n')
  fil.write('</head>\n')
  fil.write('<body>\n')
  return fil

def doc_close(fil=''):
  fil.write('</body>\n')
  fil.write('</html>\n')
  fil.close()
 
print("Número de parámetros: ", len(sys.argv))
print("Lista de argumentos: ", sys.argv)

file = sys.argv[1]

fil = open(file, 'r')

datos = fil.readlines()

fil.close()

filo = doc('salida.html', 'holas')

pref = 'sss'
n = 1
for ss in datos:
  print(ss)
  ssn = '<p> <a href="' + ss + '">' + pref + str(n) + '</a>' + '</p>\n'
  filo.write(ssn)
  n = n+1
doc_close(filo)





