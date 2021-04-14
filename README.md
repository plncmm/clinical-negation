# Clinical Negation Detector

## Instalación

1. Crear un ambiente virtual de python e instalar los requerimientos del `requirements.txt`
2. Lanzar el servidor de detección de negaciones con el comando `<ubicación de los binarios del ambiente virtual>/uvicorn main:app`

## Utilización

Este servicio web expone un único endpoint `/detector`. Para consultar si una frase está negada dado un contexto, se debe enviar una petición GET al respectivo endpoint con la frase a consultar en el parámetro `p` y el contexto en el parámetro `c`

El servicio responderá con un objeto con la propiedad `negated`, el valor de esta propiedad es `true` si la frase está negada dentro del contexto y `false` cuando no está negada dentro del contexto.

## Ejemplo de utilización

Teniendo el contexto

*TIROIDECTOMIA TOTAL: HIPERPLASIA NODULAR COLOIDEA, MULTIFOCAL BILATERAL MACRO Y MICROFOLICULAR. UN PEQUEÑO CARCINOMA PAPILAR, DEL LOBULO IZQUIERDO DE 0,3 cm. NO TIENE IMAGENES DE COMPROMISO LINFOVASCULAR NI EXTENSION EXTRATIROIDEA. ESTE NO FUE VISTO EN BIOPSIA INTRAOPERATORIA*

si necesito consultar si la frase *COMPROMISO LINFOVASCULAR* está negada dentro del contexto se debe realizar la siguiente petición:

```bash
curl --location --request GET 'http(s)://<server url>/detector?c=TIROIDECTOMIA%20TOTAL:%20HIPERPLASIA%20NODULAR%20COLOIDEA,%20MULTIFOCAL%20BILATERAL%20MACRO%20Y%20MICROFOLICULAR.%20UN%20PEQUE%C3%91O%20CARCINOMA%20PAPILAR,%20DEL%20LOBULO%20IZQUIERDO%20DE%200,3%20cm.%20NO%20TIENE%20IMAGENES%20DE%20COMPROMISO%20LINFOVASCULAR%20NI%20EXTENSION%20EXTRATIROIDEA.%20ESTE%20NO%20FUE%20VISTO%20EN%20BIOPSIA%20INTRAOPERATORIA&p=COMPROMISO%20LINFOVASCULAR'
```

y la respuesta será la siguiente:

```javascript
{
    "negated": true
}
```