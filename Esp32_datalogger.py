import network
import time
import urequests as requests
import random
from machine import Pin

# Configuración de la red Wi-Fi
ssid = "TU_SSID"
password = "TU_PASSWORD"

# Configuración del LED en el pin 2
led = Pin(2, Pin.OUT)

# Conexión a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print("Conectando a la red Wi-Fi...")
    
    while not wlan.isconnected():
        pass

    print("Conexión exitosa")
    print("IP:", wlan.ifconfig()[0])
    
    # Parpadeo del LED como confirmación
    for _ in range(5):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)

conectar_wifi()

# URL del Google Apps Script
url = "URL_DE_LA_APLICACION_WEB"

# Bucle para enviar datos
while True:
    # Generación de datos simulados
    temperatura = random.uniform(20, 30)  # Temperatura entre 20 y 30 °C
    humedad = random.uniform(40, 60)      # Humedad entre 40 y 60 %

    # Construcción de la URL con los datos
    url_con_datos = f"{url}?temp={temperatura}&hum={humedad}"
    
    # Envío de los datos
    try:
        print("Enviando datos:", temperatura, humedad)
        respuesta = requests.get(url_con_datos)
        print("Respuesta del servidor:", respuesta.text)
    except Exception as e:
        print("Error al enviar datos:", e)
    
    # Espera de 10 segundos
    time.sleep(10)

