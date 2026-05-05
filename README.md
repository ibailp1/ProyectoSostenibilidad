# ♻️ ReciclApp – Registro de Residuos Electrónicos

> Aplicación web desarrollada por alumnos de **DAM – Cuatrovientos** para la recogida y visualización de materiales reciclables electrónicos.

---

## 📋 Descripción

**ReciclApp** es una aplicación web full-stack que permite:

- **Registrar en tiempo real** los elementos electrónicos reciclables recibidos, mediante una interfaz táctil optimizada para móvil, tablet o pantalla táctil.
- **Visualizar un dashboard** con estadísticas actualizadas automáticamente: totales globales, ranking por elemento, histórico diario y feed de últimas recepciones.
- **Persistir todos los datos** en una base de datos SQLite para su análisis posterior.

---

## 🖥️ Capturas de pantalla

| Formulario táctil | Dashboard en tiempo real |
|---|---|
| Interfaz oscura con botones grandes por categoría | Estadísticas con ranking, gráfico histórico y feed |

---

## 🏗️ Arquitectura y tecnología

```
reciclapp/
├── app.py               # Backend Flask (rutas, lógica, API REST)
├── reciclapp.db         # Base de datos SQLite (se crea automáticamente)
├── requirements.txt     # Dependencias Python
├── templates/
│   ├── formulario.html  # Interfaz de registro táctil
│   └── dashboard.html   # Dashboard de estadísticas
└── README.md
```

### Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend | **Python 3.10+** + **Flask 3.x** |
| Base de datos | **SQLite** (fichero local, sin servidor) |
| Frontend | HTML5 + CSS3 + JavaScript Vanilla |
| Fuentes | Google Fonts (Bebas Neue + DM Sans) |
| Despliegue | Cualquier servidor con Python (Railway, Render, Raspberry Pi, etc.) |

### ¿Por qué este stack?
- **Flask** es ligero, fácil de entender y de desplegar, igual que en la práctica de IoT.
- **SQLite** no requiere configuración adicional: el fichero `.db` se crea solo al arrancar.
- **Sin frameworks JS complejos** (React, Vue…): todo en Vanilla JS para facilitar la comprensión y modificación.

---

## 🚀 Instalación y ejecución local

### Requisitos previos
- Python 3.10 o superior
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/ibailp1/ProyectoSostenibilidad.git
cd reciclapp

# 2. (Recomendado) Crear entorno virtual
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Arrancar la aplicación
python app.py
```

La app estará disponible en:
- **Formulario táctil:** http://localhost:5000/
- **Dashboard:** http://localhost:5000/dashboard

## 📡 API REST

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Formulario de registro táctil |
| `GET` | `/dashboard` | Dashboard de estadísticas |
| `POST` | `/api/registrar` | Registrar elementos (JSON) |
| `GET` | `/api/stats` | Obtener todas las estadísticas (JSON) |

### Ejemplo – Registrar elementos

```bash
curl -X POST http://localhost:5000/api/registrar \
  -H "Content-Type: application/json" \
  -d '{"elementos": [{"nombre": "Ratón", "cantidad": 3}, {"nombre": "Cable USB", "cantidad": 2}]}'
```

Respuesta:
```json
{ "ok": true, "registrados": 2 }
```

### Ejemplo – Obtener estadísticas

```bash
curl http://localhost:5000/api/stats
```

---

## 🗄️ Esquema de la base de datos

```sql
CREATE TABLE registros (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    elemento    TEXT    NOT NULL,        -- Nombre del elemento (ej: "Ratón")
    cantidad    INTEGER NOT NULL DEFAULT 1,
    fecha       DATE    NOT NULL,        -- Fecha del registro (YYYY-MM-DD)
    hora        TIME    NOT NULL,        -- Hora del registro (HH:MM:SS)
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 👥 Equipo de desarrollo

| Nombre |
|---|
| Oihan bbsita BBC |
| Lil Ibai nigga |
| Mario Kawai uwu |
| Iker Tiker Miker Piker |
| Luisito No Comunica |

---

## 📄 Licencia

MIT License – libre para uso educativo y modificación.

---

*Desarrollado en el marco de la actividad de centro de DAM – IES Cuatrovientos*
