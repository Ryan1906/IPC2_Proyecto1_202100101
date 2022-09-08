from importlib.abc import TraversableResources
import graphviz as gp
class Paciente():
    def __init__(self,nombre,edad,periodos,m, infectadas, tabla0):
        self.nombre=nombre
        self.edad=edad
        self.periodos=periodos
        self.m=m
        self.infectadas=infectadas
        self.tabla0=tabla0
        self.tableros=None
        self.siguiente=None
    def getsig(self):
        return self.siguiente
    def setsig(self, siguiente):
        self.siguiente=siguiente
    def settableros(self, tablero):
        self.tableros=tablero
class LinkNode : 
    def __init__(self, data) : 
        self.data = int(data)
        self.up = None
        self.prev = None
        self.next = None
        self.down = None
    def getdata(self):
        return self.data

class DoublyLinkedList : 

    def __init__(self) :
        self.head = None
        self.size = 0
    def display(self) :
        if(self.head == None) :
            print("Empty linked list", end = "")
        else :
            front = self.head
            right = None
            while (front != None) :
                right = front 
                while (right != None) :
                    print("|", right.data, end="|")
                    right = right.next

                    print(end="\n")

                    front = front.down
    def insertData(self, matrix, rows, cols) :
        for row in range(rows):
            for col in range(cols):
                if row==0 and col==0:
                    self.head=LinkNode(matrix[0][0])
                    aux=self.head
                elif row==0:
                    newnode=LinkNode(matrix[row][col])
                    aux.next=newnode
                    newnode.prev=aux
                    aux=newnode
                elif col==0:
                    newnode=LinkNode(matrix[row][col])
                    aux.down=newnode
                    newnode.up=aux
                    aux=aux.next
                    aux2=newnode
                else:
                    newnode=LinkNode(matrix[row][col])
                    aux2.next=newnode
                    newnode.prev=aux2
                    aux.down=newnode
                    newnode.up=aux
                    aux=aux.next
                    aux2=aux2.next
                self.size+=1

            aux=self.head
            for i in range(row):
                aux=aux.down

    def siguientediag(self):
        resultado=[]
        rows=0
        cols=0
        if (self.head == None) :
            print("Empty linked list", end = "")
        else :
            front = self.head
            right = None
            while (front != None) :
                right = front
                columna=[]
                while (right != None) :
                    enfermas=0
                    if right.up!=None:
                        if right.up.data==1:
                            enfermas+=1
                    if right.next!=None:
                        if right.next.data==1:
                            enfermas+=1
                    if right.prev!=None:
                        if right.prev.data==1:
                            enfermas+=1
                    if right.down!=None:
                        if right.down.data==1:
                            enfermas+=1
                    if right.up != None and right.next!=None:
                        if right.up.next !=None:
                            if right.up.next.data==1:
                                enfermas+=1
                    if right.up != None and right.prev!=None:
                        if right.up.prev !=None:
                            if right.up.prev.data==1:
                                enfermas+=1
                    if right.down != None and right.next!=None:
                        if right.down.next !=None:
                            if right.down.next.data==1:
                                enfermas+=1
                    if right.down != None and right.prev!=None:
                        if right.down.prev !=None:
                            if right.down.prev.data==1:
                                enfermas+=1
                    if(right.data==1 and (2<=enfermas<=3)):
                        columna.append(1)
                    elif right.data==0 and enfermas==3:
                        columna.append(1)
                    else:
                        columna.append(0)
                        
                    
                    right = right.next
                    cols+=1
                resultado.append(columna)
                columna=None
                rows+=1
                    
                
                
                #  Visit to down node
                front = front.down	
        # print(end = "\n")
        return resultado

    def dibujargrafica(self,pacienteactual,periodo):
        s = gp.Digraph("EVOLCUCIÓN", filename = 'EnfermedadPaciente.gv',
                node_attr={'shape': 'record'})
        s.attr(rankdir='LR')
        s.attr('node',size='20',color = 'white')
        s.node('numero','')
        s.attr('node',size='20',color = 'black')
        s.node('numero','Período NO.'+periodo)
        grid =""
        cell = ""
        if (self.head == None) :
            print("Empty linked list", end = "")
        else :
            front = self.head
            right = None
            while (front != None) :
                right = front
                grid+="{"
                while (right != None) :
                    if right.data==1:
                        cell="/@/"
                    else:
                        cell=" "
                    right = right.next
                    grid += str(cell)+"|"
                grid = grid[:len(grid)-1]
                grid+="}|"
                
                
                front = front.down	
        grid = grid[:len(grid)-1]
        s.node("muestra",grid)
        s.attr('node',size='20',color = 'white')
        s.node('titulo','EVOLUCIÓN DE ENFERMEDAD')
        s.render(filename='Pacientes/Paciente_'+pacienteactual+'/tabla'+periodo, format="png",view=0, cleanup=1)

    

class listadetableros:
    def __init__(self):
        self.tablero = None       
        self.siguiente=None 

