# (1) llamadno los modulos a trabajar
from machine import Pin
from utime import sleep
import time

# (2) se crea los objetos

# Bombas de agua
Bomba_1 = Pin(4, Pin.OUT)
Bomba_2 = Pin(18, Pin.OUT)
Bomba_3 = Pin(19, Pin.OUT)
Bomba_4 = Pin(21, Pin.OUT)

# Ventiladores 
Motor_5 = Pin(5, Pin.OUT)
Motor_6 = Pin(5, Pin.OUT)
Motor_7 = Pin(5, Pin.OUT)



print("Bienvenido al su software")

# EL siclo y el codigo
while True:

  # Encendiendo todas las bombas de agua 
  Bomba_1.value(1)
  sleep(3) # 3 segundos
  print("Encendido Bomba 1")

  Bomba_2.value(1)
  sleep(3)
  print("Encendido Bomba 2")

  Bomba_3.value(1)
  sleep(3)
  print("Encendido Bomba 3")

  Bomba_4.value(1)
  sleep(3)
  print("Encendido Bomba 4")

  # Apagando todas las bombas de agua

  Bomba_1.value(0)
  sleep(3)
  print("Apagado Bomba 1")

  Bomba_2.value(0)
  sleep(3)
  print("Apagado Bomba 2")

  Bomba_3.value(0)
  sleep(3)
  print("Apagado Bomba 3")

  Bomba_4.value(0)
  sleep(3)
  print("Apagado Bomba 4")
