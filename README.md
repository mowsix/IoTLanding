
# IOT

Este proyecto tiene como objetivo monitorear variables ambientales mediante sensores distribuidos en la sede de la Universidad Pontificia Bolivariana.


## Despliegue

Se necesita python y pip

Instalar los requerimientos

```bash
  pip install -r requirements.txt
```
Si usas un entorno virtual

```bash
  python -m venv venv 
  venv/Scripts/activate
```

Desplegar la plataforma

```bash
  python3 -m streamlit run main.py
```


## Informacion

- Los estudiantes de la upb desarrollaron agentes y brokers para multiples sensores como radiacion solar, humedad, temperatura entre otros utilizando diferentes tecnologias como wifi y LoRa

- Esta plataforma permite visualizar las mediciones de dichos sensores, permitiendo filtrar por el tipo de sensor y garantiza el acceso unico con permisos de creacion y modificacion de los sensores


## Autores

- [@mowsix](https://www.github.com/octokatherine)
- [@balcarcelmar](https://www.github.com/octokatherine)
- [@yeisson](https://www.github.com/octokatherine)
- [@sforerod](https://www.github.com/octokatherine)

