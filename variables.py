                 
                    # --- TIPOS DE DATOS Y VARIABLES --- #
                        
                            # --- Data Types --- #


number = 10                                     # int
hello = 'Hola unicornio!'                       # string
miEquipoFavorito = 'F.C BARCELONA'              # string
myAge = 25                                      # int
x = True                                        # boolean
y = False                                       # boolean
decimal = 10.0                                  # float
dolarColombia = 4.764                           # float
nombreDeMiNovia = "❤ ❤ ❤  Sandrita ❤ ❤ ❤"  # string
miVariable = False                              # boolean
cc = 1032488904                                 # int



           # 1.Execute Python Variables - print! ... Imprimir variables
           
        
print("----  1.Execute Python Variables! ---- \n")

print(number)                                         # int
print(hello)                                          # string
print(miEquipoFavorito)                               # string
print(myAge)                                          # int
print(x)                                              # boolean
print(y)                                              # boolean
print(decimal)                                        # float
print(dolarColombia)                                  # float
print(" El amor de mi vida es : " + nombreDeMiNovia)  # string
print(miVariable)                                     # boolean
print(cc)                                             # int

print("\n")


            # 1.1 References Data Types - print! ...  Validar que tipo de dato imprime para cada variable
            
            
print("----  1.1 Execute Data Types! ---- \n")

print(type(number))                          # int
print(type(hello))                           # string
print(type(miEquipoFavorito))                # string
print(type(myAge))                           # int
print(type(x))                               # boolean
print(type(y))                               # boolean
print(type(decimal))                         # float
print(type(dolarColombia))                   # float
print(type(nombreDeMiNovia))                 # string
print(type(miVariable))                      # boolean
print(type(cc))                              # int

print("\n")


            #  2. Memory address and variables - print! ... Ver la direccion de memoria que presentan las variables
            
            
print("----  2. Memory address and variables ---- \n")

print(id(number))                          # int
print(id(hello))                           # string
print(id(miEquipoFavorito))                # string
print(id(myAge))                           # int
print(id(x))                               # boolean
print(id(y))                               # boolean
print(id(decimal))                         # float
print(id(dolarColombia))                   # float
print(id(nombreDeMiNovia))                 # string
print(id(miVariable))                      # boolean
print(id(cc))                              # int

print("\n")


                         # --- CASTEAR TIPOS DE DATOS --- #

        # 3. Python Casting Data Types to int! - Ejemplo de casteo a tipo entero
        
        
print("--- 3. Casting to int --- ")

a = int(6)        # a = 6
b = int(7.8)      # b = 7
c = int("8")      # c = 8
d = int(9.5)      # d = 9

print(a)
print(b)
print(c)
print(d)

print("\n")


       # Python Casting Data Types to string! - Ejemplo de casteo a tipo string
        
        
print("--- 3.1 Casting to string --- \n")

w = str("al-#1")    # w = 'al-#1'
x = str(9)          # x ='9'
y = str(2.1)        # y ='2.1'
z = str(3.0)        # z ='3.0'

print(w)
print(x)
print(y)
print(z)

print("\n")


       # Python Casting Data Types to float! - Ejemplo de casteo a tipo float
       
        
print("--- 3.2 Casting to float --- \n")

g = float(0)        # g = 0.0
h = float(1)        # h = 1.0
i = float(2.5)      # i = 2.5
j = float("3")      # j = 3.0
k = float("4.5")    # k = 4.5

print(g)
print(h)
print(i)
print(j)
print(k)

print("\n")


               # datetime - print! ... Imprimir tipo de fecha actual 
               
               
print("----  4. Execute Python datetime! ---- \n")
import datetime

currentDate = datetime.datetime.now()

print(currentDate)
print(type(currentDate))   #  = YYYY-MM-DD 00:00:00.#####

print("\n")
