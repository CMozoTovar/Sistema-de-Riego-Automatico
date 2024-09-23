# Sistema-de-Riego-Automatico
El proyecto consiste en un sistema de riego automático basado en un ESP32, diseñado para regar plantas de manera automática en función de los niveles de humedad en el suelo. Utiliza un sensor de humedad del suelo YL-69 para medir la humedad y, dependiendo del valor leído, activa o desactiva una bomba de agua SIG0833 controlada mediante un módulo relé SRD-12VDC. El objetivo es garantizar que las plantas reciban la cantidad adecuada de agua sin intervención manual constante.

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

