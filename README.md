
# SMART PARKING
## 1. Contexto, motivación:
El objetivo principal de este proyecto IoT es mejorar la experiencia de los
usuarios de parqueaderos, ya que la automatización del ingreso reducirá el 
tiempo de espera y aumentará la seguridad en el acceso.

## Diagrama de casos de uso
![diagrama de casos de uso](https://github.com/estebandurangov/SmartParking/blob/main/Images/casosdeuso.drawio.png)

## Descripción caso de uso más relevante
## CASO DE USO VALIDAR INGRESO
validación de ingreso de un vehículo al parqueadero inteligente utilizando sensores y reconocimiento de placa. El objetivo principal es automatizar y agilizar el proceso de registro y control de acceso al parqueadero, proporcionando una experiencia conveniente tanto para los usuarios como para los administradores del parqueadero.

## El flujo del caso de uso sería el siguiente:

1. El vehículo se acerca a la entrada del parqueadero y se activan los sensores de detección de presencia.
2. Los sensores captan la presencia del vehículo y envían una señal al sistema de reconocimiento de placa.
3. El sistema de reconocimiento de placa utiliza una cámara especializada para capturar una imagen de la placa del vehículo.
4. A continuación, el software analiza la imagen de la placa utilizando OpenCV, con reconocimiento óptico de caracteres (OCR) para extraer los caracteres alfanuméricos de la placa.
5. El sistema compara los caracteres extraídos con una base de datos interna que contiene las placas autorizadas.
6. Si la placa coincide con una placa autorizada, el software envía una señal para abrir la barrera o puerta de acceso al parqueadero.
7. En caso de que la placa no esté autorizada o se encuentre en la lista de restricción, el software registra la entrada como no válida y puede enviar una alerta al personal de seguridad.
8. Una vez que se valida la entrada, el sistema registra la hora y fecha de ingreso del vehículo junto con la placa en una base de datos interna para futuras referencias y seguimiento.

## distribución del sistema

![Diagrama de la arquitectura implementada](https://github.com/estebandurangov/SmartParking/blob/main/Images/iot%20smart%20parking.png)

## 2. Arquitectura

## Diagrama de la arquitectura
![Diagrama de la arquitectura implementada](https://github.com/estebandurangov/SmartParking/blob/main/Images/arq%20IOT.drawio.png)

## Topicos 
El MQTT Broker actúa como el intermediario de mensajería entre la Raspberry Pi y los dispositivos ESP32. Facilita la transmisión de mensajes entre ellos.
A continuación se exponen los tópicos que se usarán en MQTT

![Topics implementada](https://github.com/estebandurangov/SmartParking/blob/main/Images/topics.png)

## 3. Trabajo futuro
*Registrar la hora de ingreso de los vehículos autorizados y marcar los espacios de estacionamiento correspondientes como ocupados en la base de datos del sistema.

*Mejoras en la precisión y velocidad del reconocimiento de placa: Se puede trabajar en el desarrollo de algoritmos más avanzados y técnicas de procesamiento de imágenes para lograr una mayor precisión en el reconocimiento de placas y reducir los tiempos de respuesta. Esto permitiría una validación más rápida y confiable de los vehículos en la entrada del estacionamiento.

*Integración con sistemas de pago y reserva: Smart Parking puede evolucionar para incluir una integración completa con sistemas de pago y reserva en línea. Esto permitiría a los conductores reservar plazas de estacionamiento con anticipación y realizar pagos de manera más conveniente, ya sea a través de aplicaciones móviles, tarjetas de crédito o sistemas de pago sin contacto.

*Implementación de sensores de ocupación en tiempo real: La instalación de sensores de ocupación en cada plaza de estacionamiento permitiría monitorear en tiempo real la disponibilidad de plazas. Esto ayudaría a los conductores a encontrar rápidamente lugares vacantes y optimizar la utilización del espacio.

*Uso de analítica de datos para la gestión del estacionamiento: La recopilación y análisis de datos generados por el sistema de Smart Parking puede proporcionar información valiosa para la toma de decisiones. Se pueden utilizar herramientas de análisis de datos para comprender los patrones de uso del estacionamiento, identificar áreas de congestión, mejorar la planificación de la capacidad y optimizar la eficiencia operativa.

## 4. Guía de instalación
<img align="right" height="256" src="https://raw.githubusercontent.com/kivy/kivy/master/kivy/data/logo/kivy-icon-256.png"/>

Innovative user interfaces made easy.

Kivy is an open source, cross-platform [Python](https://www.python.org)
framework for the development of applications that make use of innovative,
multi-touch user interfaces.
The aim is to allow for quick and easy interaction design and rapid prototyping
whilst making your code reusable and deployable.

Kivy is written in Python and [Cython](http://cython.org/), based on OpenGL ES
2, supports various input devices and has an extensive widget library. With the
same codebase, you can target Windows, macOS, Linux, Android and iOS. All Kivy
widgets are built with multitouch support.

Kivy is MIT licensed, actively developed by a great community and is supported
by many projects managed by the [Kivy Organization](https://kivy.org/#organization).

[![Bountysource](https://www.bountysource.com/badge/tracker?tracker_id=42681)](https://www.bountysource.com/trackers/42681-kivy?utm_source=42681&utm_medium=shield&utm_campaign=TRACKER_BADGE)
[![Backers on Open Collective](https://opencollective.com/kivy/backers/badge.svg)](#backers)
[![Sponsors on Open Collective](https://opencollective.com/kivy/sponsors/badge.svg)](#sponsors)

[![Coverage Status](https://coveralls.io/repos/kivy/kivy/badge.svg?branch=master)](https://coveralls.io/r/kivy/kivy?branch=master)
[![Windows Unittests Status](https://github.com/kivy/kivy/workflows/Windows%20Unittests/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22Windows+Unittests%22)
[![Ubuntu Unittests Status](https://github.com/kivy/kivy/workflows/Ubuntu%20Unittests/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22Ubuntu+Unittests%22)
[![OSX Unittests Status](https://github.com/kivy/kivy/workflows/OSX%20Unittests/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22OSX+Unittests%22)
[![Windows wheels Status](https://github.com/kivy/kivy/workflows/Windows%20wheels/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22Windows+wheels%22)
[![Manylinux wheels Status](https://github.com/kivy/kivy/workflows/Manylinux%20wheels/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22Manylinux+wheels%22)
[![Raspberry Pi wheels Status](https://github.com/kivy/kivy/workflows/RPi%20wheels/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22RPi+wheels%22)
[![OSX wheels Status](https://github.com/kivy/kivy/workflows/OSX%20wheels%2Fapp/badge.svg)](https://github.com/kivy/kivy/actions?query=workflow%3A%22OSX+wheels%2Fapp%22)

Installation, Documentation and Examples
