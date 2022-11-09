
class calculadora():
    def __init__(self):
        self.resultado=0
        self.dato1=0
        self.dato2=0
    def sumar (self):
        self.resultado=self.dato1+self.dato2
    def restar(self):
        self.resultado=self.dato1-self.dato2
    def multiplicar (self):
        self.resultado=self.dato1*self.dato2
    def dividir(self):
        self.resultado=self.dato1/self.dato2

    def imprimir(self):
        return self.resultado

operar=calculadora()
operar.dato1=float(input("ingrese un digito"))
operar.dato2=float(input("ingrese un digito"))
operar.sumar()
print (str(operar.dato1) + "+" + str(operar.dato2)+ "=" + str(operar.resultado))
operar.restar()
print (str(operar.dato1)+ "-"+ str(operar.dato2)+ "="+ str(operar.resultado))
operar.dividir()
print(str(operar.dato1)+ "/" + str(operar.dato2)+ "="+ str(operar.resultado))
operar.multiplicar()
print(str(operar.dato1)+ "*" + str(operar.dato2)+ "="+ str(operar.resultado))



