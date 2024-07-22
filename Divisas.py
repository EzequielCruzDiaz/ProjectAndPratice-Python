import datetime

nombre = input("Introduzca su nombre: ")
fecha = datetime.datetime.now().strftime("%Y-%m-%d")
hora = datetime.datetime.now().hour
horatransf = datetime.datetime.now().strftime("%H:%M:%S")

dolares = float(input("Introduzca la cantidad de dolares deseada a cambiar:"))
tipo_de_cambio = 0.88


if 5 <= hora < 12:
    saludo = f"Buenos Dias {nombre}"
elif 12 <= hora < 18:
    saludo = f"Buenas Tardes {nombre}"
else:
    saludo = f"Buenas Noches {nombre}"


if dolares > 0:
    euros_a_recibir = dolares * tipo_de_cambio
else:
    euros_a_recibir = 0


print(f'{saludo},\nCantidad de dólares: {dolares}\nCantidad de euros a recibir: {euros_a_recibir:.2f}\nFecha y hora de transacción: {fecha} a las {horatransf}')
