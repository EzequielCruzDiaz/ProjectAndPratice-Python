import datetime

nombre = input("Introduzca su nombre: ")
fecha = datetime.datetime.now().strftime("%Y-%m-%d")
hora = datetime.datetime.now().hour


if 5 <= hora < 12:
    saludo = f"Buenos Dias {nombre}"
elif 12 <= hora < 18:
    saludo = f"Buenas Tardes {nombre}"
else:
    saludo = f"Buenas Noches {nombre}"


print(f'{saludo} tu transaccion fue realizada el {fecha} ')
