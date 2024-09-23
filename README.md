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
  ![image](https://github.com/user-attachments/assets/43334cbc-8589-4683-8016-7dc90dd63c35)

- Sensor de Humedad YL-69
- ![image](https://github.com/user-attachments/assets/b92fabb2-9591-40a9-a02a-d3e6a352460d)

- Módulo Relé SRD-12VDC
  ![image](https://github.com/user-attachments/assets/71da27a5-f1c7-4d80-9efd-6b22da37e28b)

- Bomba de Agua SIG0833
  ![image](https://github.com/user-attachments/assets/5f4dfe9f-d6d3-4f75-b516-e3d35a80868c)

- Fuente de 12V para la bomba
  ![image](https://github.com/user-attachments/assets/d2768439-75ad-4b8f-8918-07122186f8df)


## Instrucciones
1. Realiza las conexiones siguiendo el esquema en `/docs/circuito_diagrama.png`.
2. Carga el código desde `/src/main.cpp` en tu ESP32.
3. Ajusta los parámetros en `/src/config.h` según tu configuración.

