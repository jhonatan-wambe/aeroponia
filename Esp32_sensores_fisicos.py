import time
from machine import Pin, I2C
import dht
from bh1750 import BH1750
import network
import urequests

# Pines y configuración del DHT22
pin_dht = Pin(15)
sensor_dht = dht.DHT22(pin_dht)

# Pines y configuración del BH1750 (luminosidad)
i2c = I2C(scl=Pin(22), sda=Pin(21))  # Ajusta los pines si es necesario
sensor_luz = BH1750(i2c)

# Configuración del sensor PPM (simulado aquí)
sensor_ppm = Pin(34, Pin.IN)  # Ajusta este pin según tu configuración

# Pin para el switch que activa el envío de datos
switch_pin = Pin(12, Pin.IN)  # Pin de entrada para el switch

# Datos de conexión WiFi
SSID = "NOMBRE_RED_WIFI"
PASSWORD = "CONTRASEÑA_WIFI"

# Conexión WiFi
def conectar_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)
    while not wifi.isconnected():
        print("Conectando a la red Wi-Fi...")
        time.sleep(1)
    print("Conexión exitosa")
    print(wifi.ifconfig())

# Función para enviar datos a Google Sheets
def enviar_datos(temp, hum, luz, ppm):
    url = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"
    parametros = {
        "temperatura": temp,
        "humedad": hum,
        "luminosidad": luz,
        "ppm": ppm
    }
    try:
        respuesta = urequests.get(url, params=parametros)
        print("Datos enviados")
        print("Respuesta del servidor:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar los datos:", e)

# Configurar WiFi
conectar_wifi()

# Bucle principal
while True:
    if switch_pin.value() == 1:  # Verifica si el switch está activado
        # Leer datos de los sensores
        try:
            # DHT22: Temperatura y Humedad
            sensor_dht.measure()
            temp = sensor_dht.temperature()
            hum = sensor_dht.humidity()

            # BH1750: Luminosidad
            luz = sensor_luz.luminance(BH1750.ONCE_HIRES_1)

            # Sensor PPM (simulado como valor digital por ahora)
            ppm = sensor_ppm.value()  # Aquí deberías colocar la lógica específica para el PPM

            # Enviar datos a la hoja de cálculo
            enviar_datos(temp, hum, luz, ppm)
        except Exception as e:
            print("Error al leer los sensores:", e)
        
        # Esperar 10 segundos antes de enviar la siguiente lectura
        time.sleep(10)
    else:
        print("Switch desactivado, esperando...")
        time.sleep(1)  # Espera un segundo antes de verificar el switch de nuevo
