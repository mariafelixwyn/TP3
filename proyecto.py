from lxml import etree
from urllib.request import urlopen
import tkinter as tk
from tkinter import simpledialog
import sys
application_window = tk.Tk()
pregunta = simpledialog.askstring("Input", "Quieres guardar el filtrado en un archivo? (S/N) ",
                                parent=application_window)
pregunta = pregunta.lower()
if pregunta == "s":
	fichero = simpledialog.askstring("Input", "Como llamaras al fichero ",
                                parent=application_window)
	fs = open(fichero,"w")

	pagina = simpledialog.askstring("Input", "Que página quieres filtrar (tiene que ser XML): ",
	                                parent=application_window)
	ns={"Atom" : "http://www.w3.org/2005/Atom"}
	parser=etree.XMLParser()
	tree=etree.parse(urlopen(pagina),parser)
	for node in tree.xpath('//Atom:entry/Atom:title', namespaces=ns) :
	   print (node.text)
	   fs.write(node.text + '\n')
	fs.close()
	lista = list()
	lista2 = []
	fh = open(fichero,"r")
	line = fh.readline()
	while line:
	  words = line.split()
	  for w in words:
	    lista.append(w)
	  line = fh.readline()
	fh.close()
	fc = open("mayusculas","w")
	for i in lista:
		if i[0].isupper():
			lista2.append(i)
			fc.write(i + "\n")
	fc.close()
	print("Estas son todas las palabras mayusculas que aparecen en los titulos (se guarda el resultado en un fichero llamado mayusculas): ")
	print(lista2)

else:
	print("Ok")

