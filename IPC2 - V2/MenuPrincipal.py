from fileinput import filename
from traceback import print_list
from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
from tkinter import filedialog as fd


from Lista import Lista

print("*********Predicción Patrones Enfermedades********")
lista = Lista()
a = input("¿Desea abrir el archivo? (Si)(No)")
if a == "Si":
    print("hola")
    filename=fd.askopenfilename(initialdir="/", title="Seleccione el Archivo", filetypes=((("Archivos xml",".XML"),("Todos los archivos",".*"))))
    dcx=minidom.parse(filename)
    paciente= dcx.getElementsByTagName("paciente")
    for i in paciente:

       

        nombre = i.getElementsByTagName("nombre")
        edad = i.getElementsByTagName("edad")
        periodo = i.getElementsByTagName("periodos")
        m = i.getElementsByTagName("m")

        lista.insertlast(nombre[0].firstChild.data,edad[0].firstChild.data,periodo[0].firstChild.data, m[0].firstChild.data)
    print(lista)
    lista.printlist()
   