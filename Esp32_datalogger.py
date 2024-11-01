import network
import urequests
from machine import Pin
from time import sleep

# Configuración Wi-Fi
ssid = "TOKU"
password = "LAcomidamasdeliciosaesSOLLAconARROZYHUEVO_00"

# Configuración del LED en el pin 2
led = Pin(2, Pin.OUT)

# Conectar a la red Wi-Fi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

# Parpadeo del LED mientras se conecta
print("Conectando a la red Wi-Fi...")
while not station.isconnected():
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)

# Confirmación de conexión con parpadeo de 5 veces
print("Conexión exitosa")
for _ in range(5):
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)

# Imprimir la IP de la ESP32
print(station.ifconfig())

# URL de tu Google Apps Script
url = "https://script.google.com/macros/s/AKfycbztJIqwJjAGPGEj6bRbZ-xO_Pxa-6qKZMMxFORyDxGNYsGgeTodbNkRuCq6KaOeBBVsow/exec"

# Datos de ejemplo para enviar (puedes adaptarlos según tus datos reales de sensores)
temperatura = 25.4  # Aquí iría el dato de tu sensor
humedad = 60.2      # Aquí iría el dato de tu sensor

# Enviar datos
try:
    response = urequests.get(f"{url}?temperatura={temperatura}&humedad={humedad}")
    print("Datos enviados")
    print("Respuesta del servidor:", response.text)
    response.close()
except Exception as e:
    print("Error al enviar los datos:", e)

sleep(10)  # Espera de 10 segundos antes de volver a enviar los datos
