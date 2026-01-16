
class OperasBas:
    #Declaración de propiedades
    num1=0
    um2=0
    res=0
    #declaración del constructor this
    def __init__(self): #Self indica que se puede usar uso de la clase. Practicamente un this.
        self.num1=0
        self.um2=0
    #declaración de metodos de clase

    def suma(self):
        self.res=self.num1+self.um2
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res=self.num1-self.um2
        print("La resta es: {}".format(self.res))


def main():
    obj=OperasBas()
    obj.suma()

if __name__ == "__main__":
    main()