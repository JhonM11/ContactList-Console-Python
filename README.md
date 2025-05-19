# 📇 ContactApp - Gestor de Contactos en Consola (Python)

Aplicación de consola desarrollada en **Python** usando **Programación Orientada a Objetos (POO)**. Permite gestionar una lista de contactos almacenados en un archivo CSV de forma sencilla y organizada desde la terminal.

---

## 🧩 Características

- 📝 Agregar nuevos contactos (nombre, correo electrónico, teléfono)
- 📋 Listar contactos en formato de tabla
- 🛠️ Editar contactos existentes por ID (incluye nombre, correo y teléfono)
- ❌ Eliminar contactos por ID
- 📁 Almacena los datos en un archivo `ListContact.csv` (se genera automáticamente si no existe)
- 💡 Interfaz limpia por consola utilizando la librería `tabulate`
- 🧱 Estructura modular basada en buenas prácticas de POO

---

## 📂 Estructura del Proyecto

ListContactConsole/
├── main.py # Punto de entrada de la aplicación
├── models.py # Modelo Contact (entidad)
├── services.py # Lógica de negocio: ContactBook
├── ListContact.csv # Archivo de datos (se genera si no existe)
└── README.md # Documentación del proyecto


---

## 🚀 Instalación y uso

1. Clona el repositorio:


git clone git@github.com:JhonM11/ContactList-Console-Python.git
cd ListContactConsole

## 2. Instalación de dependicias.

pip install tabulate

python main.py
