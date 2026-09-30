nombre = input ("Cual es su nombre? ")

edad = int(input("Cual es su edad? "))

if edad < 18:
    print(f"Acceso denegado: {nombre}, eres menor de edad")
elif   18 <=  edad < 65:
    print(f"Acceso concedido: Bienvenido a la zona de adultos, {nombre}. ")
else:
    print(f"Acceso concedido con descuendo VIP para adultos mayores: Bienvenido, {nombre}")