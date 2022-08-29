from gettext import npgettext
from nodo import Paciente
import numpy as np
class Lista():
    
    def __init__(self):
        self.primero= None
        self.ultimo = None
        self.size = 0
    def insertlast(self,nombre,edad,periodos,m):


        Nuevopaciente = Paciente(nombre,edad,periodos,m)
        self.size += 1
        if self.primero is None:
            self.primero = Nuevopaciente
            self.ultimo = Nuevopaciente
        else:
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp = tmp.getsig()
            tmp.setsig(Nuevopaciente)

    def printlist(self):
        
        tmp = self.primero
        #matriz = np.array([tmp.nombre,tmp.edad,tmp.periodos,tmp.m])
        global matriz
        print(self.size)
        i = 0

        for i in matriz:

            matriz = [tmp.nombre,tmp.edad,tmp.periodos,tmp.m]
            while tmp is not None:
                print(i)
                #matriz[1]= [tmp.nombre,tmp.edad,tmp.periodos,tmp.m]
                print("nombre: ", tmp.nombre, " ","edad: ", tmp.edad, " ","periodos: ", tmp.periodos, " ", "m: ", tmp.m)
                
                

                
                
                print("nombre: ", tmp.nombre, " ","edad: ", tmp.edad, " ","periodos: ", tmp.periodos, " ", "m: ", tmp.m)
                tmp = tmp.getsig()
                

        print(matriz)
    
    def validar(self):

        tmp = self.primero
        
        print("Este es la validación")
        print("nombre: ", tmp.getsig().nombre, " ","edad: ", tmp.edad[0], " ","periodos: ", tmp.periodos[0], " ", "m: ", tmp.m)
        tmp = tmp.getsig()