# Sistema-de-Riego-Automatico
Este proyecto implementa un sistema de riego automático utilizando un ESP32, un sensor de humedad de suelo YL-69, y una bomba de agua controlada por un relé.

## Estructura del Proyecto
automatic-watering-system/
├── README.md
├── /src/
│   ├── main.py
│   └── config.py  # si necesitas mover configuraciones separadas
├── /docs/
│   ├── circuito_diagrama.png
│   ├── conexiones.md
│   └── BOM.md
├── /lib/
│   ├── libraries.json
└── LICENSE

## Componentes
- ESP32
- Sensor de Humedad YL-69
- Módulo Relé SRD-12VDC
- Bomba de Agua SIG0833
- Fuente de 12V para la bomba

## Instrucciones
1. Realiza las conexiones siguiendo el esquema en `/docs/circuito_diagrama.png`.
2. Carga el código desde `/src/main.cpp` en tu ESP32.
3. Ajusta los parámetros en `/src/config.h` según tu configuración.

