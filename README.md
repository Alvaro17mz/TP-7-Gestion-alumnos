# Gestión de Alumnos

Este proyecto es una aplicación de consola para gestionar información de alumnos. Permite realizar diversas operaciones, como agregar, modificar y eliminar alumnos, así como gestionar sus notas, faltas y amonestaciones.

## 📋 Funcionalidades

- **Mostrar todos los alumnos**: Lista los datos de todos los alumnos registrados.
- **Agregar alumno**: Permite registrar un nuevo alumno con sus datos básicos.
- **Modificar datos de un alumno**: Permite modificar información como nombre, apellido, fecha de nacimiento y tutor de un alumno.
- **Eliminar alumno**: Elimina un alumno del sistema según su DNI.
- **Agregar notas**: Añade una nueva nota a la lista de notas del alumno.
- **Agregar faltas**: Incrementa el número de faltas de un alumno.
- **Agregar amonestaciones**: Incrementa el número de amonestaciones de un alumno.

## 🚀 Cómo usarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Alvaro17mz/TP-7-Gestion-alumnos.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd gestion-alumnos
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## 🗂 Estructura del proyecto

El proyecto está dividido en los siguientes archivos principales:

- **`main.py`**: Archivo principal que contiene el menú de opciones y controla el flujo del programa.
- **`gestion/datos.py`**: Contiene las funciones para realizar las operaciones CRUD y manejar los datos de los alumnos.

## 📚 Requisitos

- Python 3.7 o superior.
- No requiere librerías adicionales (todo está hecho con módulos estándar de Python).

## 💻 Ejemplo de uso

Al iniciar la aplicación, se muestra un menú como este:

```
1. Mostrar todos los alumnos
2. Agregar alumno
3. Modificar datos
4. Eliminar alumno
5. Agregar notas
6. Agregar faltas
7. Agregar amonestaciones
8. Salir
Selecciona una opción:
```

Selecciona una opción y sigue las instrucciones en pantalla para realizar la operación deseada.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza los cambios necesarios y haz un commit:
   ```bash
   git commit -m "Agregué una nueva funcionalidad"
   ```
4. Envía tus cambios al repositorio remoto:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Abre un Pull Request y describe tus cambios.

## Licencia 📜
MIT License

```plaintext
MIT License

Copyright (c) 2024 Alvaro17mz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

