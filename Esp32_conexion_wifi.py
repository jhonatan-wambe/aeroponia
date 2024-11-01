import network
import time
import urequests
from machine import Pin
from dht import DHT22

# Configura el LED en el pin 2
led = Pin(2, Pin.OUT)

# Configuración de la red Wi-Fi
ssid = '*****'          # Nombre de la red Wi-Fi
password = 'LAcomidamasdeliciosaesSOLLAconARROZYHUEVO_00' # Contraseña de la red Wi-Fi

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_retries = 10
    retries = 0
    while not wlan.isconnected() and retries < max_retries:
        print("Conectando a Wi-Fi...")
        retries += 1
        time.sleep(1)

    # Verifica si la conexión fue exitosa
    if wlan.isconnected():
        print("Conexión exitosa:", wlan.ifconfig())
        
        # LED parpadea en caso de éxito
        for _ in range(10):  # Parpadea 10 veces
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(0.5)
    else:
        print("No se pudo conectar a la red Wi-Fi")

# Llama a la función para conectarse
connect_wifi()
