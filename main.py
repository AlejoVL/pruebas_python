#Ejercicio 1

#Definimos la clase (En éste caso Decimal) para convertir a romano
class Decimal:

    #Definimos el metodo contructor con la variable numero publica    
    def __init__(self, numero):
        self.numero = numero

    #Creamos el metodo para hacer la conversion de decimal a romano
    def convertirRomano(self):

        num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
      
        while self.numero:
            div = self.numero // num[i]
            self.numero %= num[i]
    
            while div:
                print(sym[i], end = "")
                div -= 1
            i -= 1

# decimal1 = Decimal(int(input()))
# decimal1.convertirRomano()


#Ejercicio 2

#Definimos la clase (En éste caso Romano) para convertir a decimal
class Romano:

    #Definimos el metodo constructor con el atributo caracteres publico
    def __init__(self, caracteres):
        self.caracteres = caracteres

    #Definimos el metodo que nos convierta de romano a decimal
    def convertir(self):        
        romanos = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0
        i = 12
        valor = self.caracteres
        for i in range(len(valor)):
            if romanos[valor[i]] > romanos[valor[i - 1]]:
                entero += romanos[valor[i]] - 2 * romanos[valor[i - 1]]
            else:
                entero += romanos[valor[i]]
        print(entero + 10) 
    
# romano1 = Romano("CCCXLV")
# romano1.convertir()

#Ejercicio 3

#Definimos la clase cadena
class Cadena:

    #Definimos el metodo constructor con los atributos a,b,c,d,e,f,g,h públicos
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f    

    #Definimos el metodo que encuentre la validez de la cadena
    def validar(self):
        if (self.a == '(' and self.b == ')') and (self.c == '{' and self.d == '}') and (self.e == '[' and self.f == ']') or (self.a == '{' and self.b == '}') and (self.c == '(' and self.d == ')') and (self.e == '[' and self.f == ']') or (self.a == '[' and self.b == ']') and (self.c == '(' and self.d == ')') and (self.e == '{' and self.f == '}'):
            print("La cadena es valida!")

        else:
            print("Cadena Incorrecta.")

# cadena1 = Cadena('(',')','{','}','[',']')
# cadena1.validar()

#Ejercicio 4

#Definimos la clase 
class SubConjuntos:

    #Definimos el metodo constructor
    def __init__(self, numeros):
        self.numeros = numeros

    #Definimos el metodo que obtiene los posibles subconjuntos
    def obtener_subconjuntos(self):
        n = len(self.numeros)
        subconjuntos = [[]]

        for i in range(n):
            for j in range(len(subconjuntos)):
                subconjunto = subconjuntos[j] + [self.numeros[i]]
                if subconjunto not in subconjuntos:
                    subconjuntos.append(subconjunto)
        
        print(subconjuntos)

# conjunto1 = SubConjuntos([4,5,6])
# conjunto1.obtener_subconjuntos()

#Ejercicio 5

#Definimos la clase
class EncontrarParSuma:
    def __init__(self, numeros, objetivo):
        self.numeros = numeros
        self.objetivo = objetivo

    #Definimos el metodo que encuentre la los números que su suma sea 50(objetivo)
    #por medio de sus indices dentro de la matriz
    def encontrar_par_suma(self):
        indice1 = -1
        indice2 = -1
        n = len(self.numeros)
        for i in range(n):
            for j in range(i+1, n):
                if self.numeros[i] + self.numeros[j] == self.objetivo:
                    indice1 = i
                    indice2 = j
                    break
            if indice1 != -1:
                break
        print(indice1, indice2)

matriz1 = EncontrarParSuma([10,20,10,40,50,60,70], 50)
matriz1.encontrar_par_suma()

#Ejercicio 6

#Definimos la clase
class SumaCero:

    #Definimos el metodo constructor
    def __init__(self, numeros):
        self.numeros = numeros

    #Creamos el metodo para encontrar que números su suma da 0
    def encontrar_suma_cero(self):
        resultados = []
        n = len(self.numeros)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.numeros[i] + self.numeros[j] + self.numeros[k] == 0:
                        resultados.append([self.numeros[i], self.numeros[j], self.numeros[k]])
        print(resultados)

# conjunto1 = SumaCero([-25, -10, -7, -3, 2, 4, 8, 10])
# conjunto1.encontrar_suma_cero()

#Ejercicio 7

#Definimos la clase
class Numero:

    #Definimos el metodo constructor
    def __init__(self, x, n):
        self.x = x
        self.n = n

    #Creamos el metodo para la operacion donde x es la base y n el exponente
    def exponente(self):
        result = self.x ** self.n
        print("El resultado de la operacion siendo x =", self.x, "(La base)\ny n =", self.n, "(como exponente)\nEs: {}".format(result))

# numero1 = Numero(3,5)
# numero1.exponente()

#Ejercicio 8

#Definimos la clase
class RevertidorDeCadena:

    #Creamos el metodo contructor
    def __init__(self, cadena):
        self.cadena = cadena

    #Creamos el metodo para poder revertir el orden de la cadena de caracteres
    def revertir(self):
        palabras = self.cadena.split()
        palabras_revertidas = palabras[::-1]
        cadena_revertida = " ".join(palabras_revertidas)
        print("El resultado es " + cadena_revertida)
    
# palabra1 = RevertidorDeCadena("Mi Diario Python")
# palabra1.revertir()

#Ejercicio 9

#Definimos la clase
class Cadena:

    #Definimos el metodo constructor
    def __init__(self):
        self.cadena = ""

    #Definimos el metodo para obtener la cadena de texto
    def get_string(self):
        self.cadena = input("Ingresa el texto que desees: ")

    #Definimos el metodo que nos muestra la cadena de texto ingresada con los caracteres en mayuscula
    def set_string(self):
        print(self.cadena.upper())

# cadena1 = Cadena()
# cadena1.get_string()
# cadena1.set_string()

#Ejercicio 10

#Definimos la clase
class Rectangulo:

    #Definimos el metodo constructor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #Definimos el metodo que calcula el a´rea del rectangulo
    def area(self):
        area = self.base * self.altura
        print("El área del rectuangulo es: ", area)

# rectangulo1 = Rectangulo(5, 3)
# rectangulo1.area()

#Ejericio 11

#Definimos la clase
class Circulo:

    #Definimos el metodo constructor
    def __init__(self, radio):
        self.radio = radio
    
    #Definimos el metodo que calcula el área del circulo
    def area(self):
        pi = 3.14
        area = pi * (self.radio ** 2)
        print("El área del circulo es de", area)

    #Definimos el metodo que calcula el perimetro del circulo
    def perimetro(self):  
        pi = 3.14      
        diametro = self.radio * 2
        perimetro = pi * diametro
        print("El perimetro del circulo es de", perimetro)

# circulo1 = Circulo(5)
# circulo1.area()
# circulo1.perimetro()