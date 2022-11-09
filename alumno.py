

class Alumno :
    def __init__(self):
        self.nombre=input("nombre del alumno")
        self.nota=float(input("nota del alumno"))

    def mostrar(self):
        print("nombre",self.nombre)
        print("nota",self.nota)

    def EstudianteNota (self):
        if self.nota >= 3:
            print("has sido aprobado")
        else:
            print("no has aprobado")
    
alumno1=Alumno()
alumno1.mostrar()
alumno1.EstudianteNota()









