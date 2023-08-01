"argumentos en una fucnion"

def suma(operando1,operando2):
    return operando1+operando2
print(suma(7,5))

def resta(operando1,operando2):
    return operando1-operando2
print(resta(7,5))

def resta(a=0,b=0):
    return a-b
print (resta())
"argumento por valor y referencia"

def duplicar_numero(numero):
        numero *=2
        return numero
num=30
print(duplicar_numero(num))

def duplicar_numeros(lista_de_numeros):
          for i,n in enumerate(lista_de_numeros):
               lista_de_numeros[i] *=2
          return lista_de_numeros
 
lista_de_pedro = [1,2,3,4]
print(duplicar_numeros(lista_de_pedro))

"*args"
def sumar(*args):
      resultado = 0
      for valor in args:
            resultado+=valor
      return print (resultado )
sumar(1,2)
sumar(2,3,4,5,6,7,8,9,10)

"**kwars"
def sumar(**kwars):
      resultado = 0
      for clave, valor in kwars.items():
            print(clave, "=", valor)
            resultado +=valor
      return print(resultado)
sumar(a=21, b=32, c=45)
