# Manual de Uso: Sistema Solar en VTK

## Introducción

Este manual describe cómo utilizar la aplicación del sistema solar implementada en Python usando VTK. La aplicación permite visualizar y simular el sistema solar con planetas y satélites orbitando alrededor del Sol.

## Escalado Real

Si desea visualizar el sistema solar a una escala realista, pero usando los valores descritos en el JSON proporcionado:

```sh
python main.py <descriptor.json> 
```
si tomamos el radio del Sol como n, podemos expresar los tamaños de los radios y las órbitas de los planetas en función de n. Aquí tienes las proporciones:

Radios de los Planetas en Función de n
Mercurio: 
0.0035*n

Venus: 
0.0087*n

Tierra: 
0.0091*n

Marte: 
0.0049*n

Júpiter: 
0.1005*n

Saturno: 
0.0836*n

Urano: 
0.0364*n

Neptuno: 
0.0354*n

Orbitas de los Planetas en Función de n
Mercurio: 
83.14*n

Venus: 
155.46*n

Tierra: 
214.95*n

Marte: 
327.57*n

Júpiter: 
1118.34*n

Saturno: 
2060.44*n

Urano: 
4127.81*n

Neptuno: 
6462.69*n

Estas proporciones permiten escalar adecuadamente el sistema solar para que mantenga su realismo, asegurando que tanto los radios como las órbitas de los planetas sean proporcionales al tamaño del Sol. 🚀🌌

## Escalado Real

Si desea visualizar el sistema solar a una escala no realista pero que se ve un poco mejor, aunque manteniendo proporciones, usando los valores distintos en el JSON proporcionado:

```sh
python main2.py <descriptor.json> 
```

## Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:
- Python
- VTK

Para instalar VTK, usa el siguiente comando:
```sh
pip install vtk
```


## Estructura de Archivos

main.py: Archivo principal que ejecuta la aplicación.

planet.py: Define la clase Planet que representa los planetas y sus comportamientos.

textures/: Carpeta que contiene las imágenes de textura para los planetas y el Sol.

descriptor.json: Archivo JSON que describe el sistema solar.

## Formato del Archivo JSON
El archivo JSON debe tener el siguiente formato:

json

Copiar
{
  "Sun": {
    "size": "696340",
    "planets": {
      "Mercury": {
        "size": "2440",
        "orbit": "57.91e6",
        "period": "0.240846"
      },
      "Venus": {
        "size": "6052",
        "orbit": "108.2e6",
        "period": "0.615"
      },
      "Earth": {
        "size": "6371",
        "orbit": "149.6e6",
        "period": "1",
        "satellites": {
          "Moon": {
            "size": "1737",
            "orbit": "0.3844e6",
            "period": "0.0748"
          }
        }
      },
      "Mars": {
        "size": "3390",
        "orbit": "227.9e6",
        "period": "1.881"
      },
      "Jupiter": {
        "size": "69911",
        "orbit": "778.5e6",
        "period": "11.86"
      },
      "Saturn": {
        "size": "58232",
        "orbit": "1.434e9",
        "period": "29.46"
      },
      "Uranus": {
        "size": "25362",
        "orbit": "2.871e9",
        "period": "84.01"
      },
      "Neptune": {
        "size": "24622",
        "orbit": "4.495e9",
        "period": "164.8"
      }
    }
  }
}

## Funcionalidades

### Visualización
La aplicación renderiza una visualización del sistema solar en una ventana de VTK. Los planetas y satélites orbitan alrededor del Sol en tiempo real.


### Interacción
Puedes interactuar con la visualización usando el ratón para rotar y hacer zoom.

### Notas
Asegúrate de que las rutas de las texturas sean correctas y que las imágenes estén disponibles en la carpeta textures.

Puedes ajustar los parámetros de escala en el código para adaptarlos mejor a tus necesidades visuales.

