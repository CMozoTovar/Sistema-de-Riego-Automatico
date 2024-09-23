from machine import Pin, ADC
import time

# Configuración de pines
sensor_humedad = ADC(Pin(34))  # Pin para el sensor YL-69
sensor_humedad.atten(ADC.ATTN_11DB)  # Ajuste de rango de 0 a 3.3V

rele_bomba = Pin(26, Pin.OUT)  # Pin para controlar el relé de la bomba

# Umbral de humedad
HUMIDITY_THRESHOLD = 600

while True:
    # Leer valor del sensor de humedad
    valor_humedad = sensor_humedad.read()
    print("Humedad del suelo:", valor_humedad)

    # Control de la bomba basado en la humedad
    if valor_humedad < HUMIDITY_THRESHOLD:
        rele_bomba.on()  # Enciende la bomba
        print("Bomba encendida.")
    else:
        rele_bomba.off()  # Apaga la bomba
        print("Bomba apagada.")

    time.sleep(2)  # Esperar 2 segundos antes de la siguiente lectura
