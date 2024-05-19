<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Repositorio Autodidáctico de Proyectos en Python</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background: white;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #333;
            color: #f4f4f4;
            padding: 10px;
            overflow: auto;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Repositorio Autodidáctico de Proyectos en Python</h1>
        <p>¡Bienvenido al repositorio autodidáctico de <strong>Proyectos en Python</strong>! Aquí encontrarás una colección de proyectos desarrollados en Python, junto con guías y ejemplos para ayudarte a comenzar con tus propios proyectos. Este repositorio es ideal tanto para principiantes como para desarrolladores experimentados que buscan inspiración o ejemplos de código.</p>

        <h2>Tabla de Contenidos</h2>
        <ul>
            <li><a href="#descripción">Descripción</a></li>
            <li><a href="#instalación">Instalación</a></li>
            <li><a href="#proyectos">Proyectos</a></li>
            <li><a href="#contribuciones">Contribuciones</a></li>
            <li><a href="#contacto">Contacto</a></li>
        </ul>

        <h2 id="descripción">Descripción</h2>
        <p>Este repositorio contiene diversos proyectos en Python que abarcan diferentes niveles de dificultad y áreas de aplicación, desde scripts simples hasta aplicaciones más complejas. Cada proyecto incluye:</p>
        <ul>
            <li>Descripción del proyecto</li>
            <li>Requisitos</li>
            <li>Instrucciones de instalación y uso</li>
            <li>Ejemplos de código</li>
            <li>Documentación adicional (si aplica)</li>
        </ul>

        <h2 id="instalación">Instalación</h2>
        <p>Para comenzar con estos proyectos, sigue los siguientes pasos:</p>
        <ol>
            <li><p><strong>Clonar el repositorio:</strong></p>
                <pre><code>git clone https://github.com/tu-usuario/creacion-proyectos-python.git
cd creacion-proyectos-python</code></pre>
            </li>
            <li><p><strong>Crear un entorno virtual (opcional pero recomendado):</strong></p>
                <pre><code>python -m venv venv
source venv/bin/activate   # En Windows usa `venv\Scripts\activate`</code></pre>
            </li>
            <li><p><strong>Instalar las dependencias necesarias:</strong></p>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
        </ol>

        <h2 id="proyectos">Proyectos</h2>

        <h3>1. Enviar Correos Automáticos</h3>
        <ul>
            <li><strong>Descripción:</strong> Un script para enviar correos electrónicos de manera automática.</li>
            <li><strong>Tecnologías:</strong> Python, smtplib, email</li>
            <li><strong>Instrucciones:</strong></li>
            <pre><code>cd enviar_correos_automaticos
python enviar_correo.py</code></pre>
            <li><strong>Requisitos:</strong> Configura tus credenciales de correo en el archivo <code>config.py</code>.</li>
            <li><strong>Código:</strong></li>
            <pre><code>import smtplib
from email.mime.text import MIMEText

subject = "Test message"
body = "your message here"
sender = "your email here "
recipients=["Destiny email here"]
password="your gmail api password here"

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = sender
    msg['To'] = ''.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)</code></pre>
        </ul>

        <h3>2. Asistente Virtual Sencillo</h3>
        <ul>
            <li><strong>Descripción:</strong> Un asistente virtual básico que puede responder a comandos de voz.</li>
            <li><strong>Tecnologías:</strong> Python, SpeechRecognition, pyttsx3</li>
            <li><strong>Instrucciones:</strong></li>
            <pre><code>cd asistente_virtual
python asistente_virtual.py</code></pre>
            <li><strong>Requisitos:</strong> Asegúrate de tener un micrófono configurado y los paquetes necesarios instalados.</li>
            <li><strong>Código:</strong></li>
            <pre><code>import pyjokes
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import datetime
import time
import speech_recognition as sr
import subprocess
import pyautogui
import threading
import openai
from pathlib import Path

openai.api_key = "YOUR API KEY"
voz = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0"

def transformar_audio_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("ya puedes hablar")
        audio = r.listen(origen)

        try:
            pedido = r.recognize_google(audio, language="es-mx")
            print("Dijiste: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("Uis... No entendí")
            hablar("Disculpa, no te he entendido")
            return "sigo esperando"

        except sr.RequestError:
            print(f"Uis... No hay servicio")
            return "sigo esperando"

        except:
            print("Uis... Algo salió mal")
            return "sigo esperando"

def obtener_respuesta(pregunta):
    try:
        respuesta_creada = openai.completions.create(
            engine = "text-davinci-002",
            prompt=pregunta,
            max_tokens=150
            
        )
        return respuesta_creada.choices[0].text.strip()
    
    except  Exception as e:
        print(f"Error al obtener respuesta{e}")
        return "Lo siento, hubo un error al procesar tu solicitud"

def buscar_en_internet(pedido):
    hablar("ya mismo estoy en eso")
    pedido = pedido.replace("buscar en internet")
    threading.Thread(target=buscar_en_internet_thread, args=(pedido,)).start()

def buscar_en_internet_thread(pedido):
    pywhatkit.search(pedido)
    hablar("Esto es lo que he encontrado")

def hablar(mensaje):
    engine = pyttsx3.init()
    engine.setProperty("voice", voz)
    engine.say(mensaje)
    engine.runAndWait()

def pedir_dia():
    dia = datetime.datetime.today()
    print(dia)

    dia_semana = dia.weekday()
    mes_actual = dia.month
    print(dia_semana)

    calendario = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo",
    }

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    hablar(f"Hoy es {calendario[dia_semana]} {dia.day} de {meses[mes_actual]}")

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f" En este momento son las {hora.hour} horas con {hora.minute} minutos"
    print(hora)
    hablar(hora)

def pedir_informacion():
    hablar("Hola, ¿Cómo te llamas?")
    nombre = transformar_audio_texto()
    hablar(f"¡Hola {nombre}! ¿Cómo te sientes hoy?")
    animo = transformar_audio_texto()
    return nombre, animo

def saludo_inicial(nombre, animo):
    hora_actual = datetime.datetime.now()

    if 6 <= hora_actual.hour < 12:
        momento = f"Buenos días {nombre}"
    elif 12 <= hora_actual.hour < 18:
        momento = f"Buenas Tardes {nombre}"
    else:
        momento = f"Buenas noches {nombre}"

    hablar(f"{momento}, Soy harmony, tu asistente virtual.")
    
    if animo.lower() in ["muy bien" , "bien" , "excelente"]:
        return hablar(f"Excelente escuchar eso {nombre}, que deseas hacer para continuar con este grandioso dia ")
    
    elif animo.lower()  in ["triste" , "mal"]:
        return hablar(f"lamento que te encuentres {animo}, vamos a escuchar tu musica favorita o iniciar la app que te gusta, para subir ese animo")
    
    else:
        hablar(f"Desplegare el menu de opciones.")

def pedir_aplicacion():
    lista_rutas = []
    lista_nombres = []
    ruta = Path("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")

    for app in ruta.glob("**/*.lnk"):
        lista_rutas.append(app)
        lista_nombres.append(app.stem.lower())

    return lista_nombres, lista_rutas

def abrir_aplicacion(pedido, nombres, rutas):
    try:
        indice_ruta_seleccionada = nombres.index(pedido)
        aplicacion = rutas[indice_ruta_seleccionada]
        threading.Thread(target=abrir_aplicacion_thread, args=(aplicacion,)).start()
    except ValueError:
        hablar("No he encontrado esa aplicación. Inténtalo otra vez")

def abrir_aplicacion_thread(aplicacion):
    subprocess.Popen(fr'"{aplicacion}"', shell=True)

def abrir_navegador(pedido):
    subprocess.Popen(fr'start opera {pedido}', shell=True)

def pedir_cosas():
    nombre, animo = pedir_informacion()
    saludo_inicial(nombre, animo)

    comenzar = True
    mientras comenzar:
        print("\nSelecciona una Opcion:")
        print("1. Buscar en Internet")
        print("2. Abrir aplicación")
        print("3. Buscar Noticias")
        print("4. Pedir la fecha")
        print("5. Pedir la hora")
        print("6. Buscar en Wikipedia")
        print("7. Reproducir música")
        print("8. Contar un chiste")
        print("9. Enviar un mensaje")
        print("10. Salir")

        pedido = transformar_audio_texto()

        if "internet" in pedido:
           buscar_en_internet(pedido)
           continue

        elif "aplicación" in pedido:
            nombres, rutas = pedir_aplicacion()
            hablar("Muy bien, ¿qué aplicación deseas abrir?")
            pedido = transformar_audio_texto().lower()
            hablar(f"Abriendo {pedido}")
            abrir_aplicacion(pedido, nombres, rutas)
            continue

        elif "noticias" in pedido:
            webbrowser.open("https://www.diariolibre.com")

        elif "fecha" en pedido:
            pedir_dia()
            continue

        elif "hora" en pedido:
            pedir_hora()
            continue

        elif "wikipedia" en pedido:
            hablar("Buscando en Wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(resultado)
            continuar

        elif "reproduce" en pedido:
            pywhatkit.playonyt(pedido)
            continuar

        elif "chiste" en pedido:
            hablar(pyjokes.get_joke("es"))
            continuar

        elif "mensaje" en pedido:
            hablar("Enviando el mensaje")
            mensaje = transformar_audio_texto().split("diga")[-1].strip()
            pywhatkit.sendwhatmsg_instantly("+18299673641", mensaje)
            time.sleep(5)
            pyautogui.press("enter")
            continuar

        elif "Eso es todo" en pedido:
            hablar("Claro, ya sabes donde encontrarme")
            comenzar = False

        else:
            hablar("Lo siento, no entiendo esa opción. Por favor, selecciona una opción válida.")

pedir_cosas()</code></pre>
        </ul>

        <h3>3. Generador de Imágenes</h3>
        <ul>
            <li><strong>Descripción:</strong> Una aplicación para generar imágenes aleatorias de diferentes categorías usando la API de Unsplash.</li>
            <li><strong>Tecnologías:</strong> Python, Tkinter, requests, PIL, ttkbootstrap</li>
            <li><strong>Instrucciones:</strong></li>
            <pre><code>cd generador_imagenes
python generador_imagenes.py</code></pre>
            <li><strong>Requisitos:</strong> Asegúrate de tener una clave API de Unsplash configurada en el script.</li>
            <li><strong>Código:</strong></li>
            <pre><code>import requests
import tkinter as tk 
import io 
import tkinter as ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

root = tk.Tk()
root.title("Image Generator")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False,False)
style = Style(theme="sandstone")

def display_image(category):
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=Y6m15_TVQEt-Tu3EgDrIzQJH5ZZAAMZe72izLDTUFpY"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
    label.config(image=photo)
    label.image = photo

def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() !="Choose Category" else "disabled")

def create_gui():
    global category_var, generate_button, label

    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")
    category_dropdown.config(width=14)

    generate_button = ttk.Button(text="Generate
