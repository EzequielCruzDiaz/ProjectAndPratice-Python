import datetime

nombre = input("Introduzca su nombre: ")
fecha = datetime.datetime.now().strftime("%Y-%m-%d")
hora = datetime.datetime.now().hour
dolares = int(input("Introduzca la cantidad de dolares deseada a cambiar:"))


if 5 <= hora < 12:
    saludo = f"Buenos Dias {nombre}"
elif 12 <= hora < 18:
    saludo = f"Buenas Tardes {nombre}"
else:
    saludo = f"Buenas Noches {nombre}"


print(f'{saludo}, \n Cantidad de dolares:{dolares} \n tu transaccion fue realizada el {fecha} ')
