from Nodo import Paciente
class listasimple():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size =0
    def insertlast(self,nombre,edad,periodos,m, infectadas, tabla0):


        newpaciente=Paciente(nombre,edad,periodos,m, infectadas, tabla0)
        self.size += 1
        if self.primero is None:
            self.primero = newpaciente
            self.ultimo = newpaciente
        else: 
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp=tmp.getsig()
            tmp.setsig(newpaciente)
    def printlist(self):
        tmp=self.primero
        print(self.size)
        while tmp is not None:
            print("Nombre: ", tmp.nombre, " ", "Edad: ", tmp.edad," ","periodos: ", tmp.periodos," ","M: ", tmp.m, " ","infectadas: ", tmp.infectadas, " ", "tabla0: ", tmp.tabla0)
            tmp=tmp.getsig()   
    def getpacientes(self, nombre):
        tmp=self.primero
        for i in range(self.size):
            if tmp.nombre==nombre:
                print("Nombre: ", tmp.nombre, " ", "Edad: ", tmp.edad," ","periodos: ", tmp.periodos," ","M: ", tmp.m, " ","infectadas: ", "\n" , tmp.infectadas, "\n", "tabla0: ","\n", tmp.tabla0)                 
                return tmp
            tmp=tmp.getsig()
    def gettabla0(self, nombre): 
        tmp=self.primero
        for i in range(self.size):
            if tmp.nombre==nombre:
                return tmp.tabla0
            tmp=tmp.getsig()       