
# SMART PARKING
## 1. Contexto, motivación:
El objetivo principal de este proyecto IoT es mejorar la experiencia de los
usuarios de parqueaderos, ya que la automatización del ingreso reducirá el 
tiempo de espera y aumentará la seguridad en el acceso.

## Diagrama de casos de uso
![diagrama de casos de uso](https://github.com/estebandurangov/SmartParking/blob/main/casosdeuso.drawio.png)

# Descripción caso de uso más relevante
# CASO DE USO VALIDAR INGRESO
validación de ingreso de un vehículo al parqueadero inteligente utilizando sensores y reconocimiento de placa. El objetivo principal es automatizar y agilizar el proceso de registro y control de acceso al parqueadero, proporcionando una experiencia conveniente tanto para los usuarios como para los administradores del parqueadero.

# El flujo del caso de uso sería el siguiente:

1. El vehículo se acerca a la entrada del parqueadero y se activan los sensores de detección de presencia.
2. Los sensores captan la presencia del vehículo y envían una señal al sistema de reconocimiento de placa.
3. El sistema de reconocimiento de placa utiliza una cámara especializada para capturar una imagen de la placa del vehículo.
4. A continuación, el software analiza la imagen de la placa utilizando OpenCV, con reconocimiento óptico de caracteres (OCR) para extraer los caracteres alfanuméricos de la placa.
5. El sistema compara los caracteres extraídos con una base de datos interna que contiene las placas autorizadas.
6. Si la placa coincide con una placa autorizada, el software envía una señal para abrir la barrera o puerta de acceso al parqueadero.
7. En caso de que la placa no esté autorizada o se encuentre en la lista de restricción, el software registra la entrada como no válida y puede enviar una alerta al personal de seguridad.
8. Una vez que se valida la entrada, el sistema registra la hora y fecha de ingreso del vehículo junto con la placa en una base de datos interna para futuras referencias y seguimiento.

Este caso de uso de validar ingreso de un vehículo por medio de sensores y reconocimiento de placa a un parqueadero inteligente ofrece una forma eficiente y segura de gestionar el acceso de vehículos al parqueadero, reduciendo los tiempos de espera y proporcionando un control automatizado y preciso.

## distribución del sistema

![Diagrama de la arquitectura implementada](https://github.com/estebandurangov/SmartParking/blob/main/iot%20smart%20parking.png)

## 2. Arquitectura

## Diagrama de la arquitectura
![Diagrama de la arquitectura implementada](https://github.com/estebandurangov/SmartParking/blob/main/arqiot.png)

Definición tópicos que se usaraán en mqtt

## 3. Trabajo futuro
El trabajo futuro del presente sistema de estacionamiento inteligente se enfocará en mejorar la precisión, eficiencia y conveniencia del proceso de estacionamiento a través de tecnologías avanzadas, integración de sistemas y enfoques sostenibles, Agregar una interfaz para el registro manual de vehiculos. Esto brindará beneficios tanto a los usuarios como a los administradores del estacionamiento, mejorando la experiencia general de estacionamiento en entornos urbanos.
Agregar análisis de datos históricos y en tiempo real, para lograr que el sistema de estacionamiento inteligente pueda predecir y gestionar la demanda de espacios de estacionamiento de manera más efectiva. Esto puede incluir la implementación de tarifas variables según la demanda, la identificación de patrones de uso y la optimización del espacio disponible.

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
