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
git clone https://github.com/TU_USUARIO/reciclapp.git
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

---

## 🌍 Despliegue en producción

### Opción A – Railway (recomendado, gratuito)

1. Crear cuenta en [railway.app](https://railway.app)
2. Conectar el repositorio GitHub
3. Railway detecta Flask automáticamente
4. Añadir variable de entorno: `PORT=5000`
5. ¡Listo! La URL pública se genera automáticamente.

> **Nota:** Para producción con Railway u otros servicios PaaS, sustituir SQLite por **PostgreSQL** (Railway lo provee gratis). Ver sección "Cómo continuar".

### Opción B – Render

1. Crear cuenta en [render.com](https://render.com)
2. Nuevo servicio Web → conectar repo GitHub
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python app.py`

### Opción C – Raspberry Pi / servidor local

```bash
# Instalar en una RPi con Raspberry Pi OS
sudo apt update && sudo apt install python3-pip -y
pip3 install -r requirements.txt
python3 app.py &   # Ejecutar en background
```

Acceder desde cualquier dispositivo de la red local en `http://IP_RASPBERRY:5000`

---

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

---

## 🔧 Cómo continuar el proyecto

### Funcionalidades sugeridas para ampliar la nota

1. **Autenticación de usuarios** – Flask-Login para que cada grupo/voluntario tenga su sesión.
2. **Exportar a CSV/Excel** – Botón en el dashboard para descargar los datos del día.
3. **Modo offline / PWA** – Service Worker para que funcione sin conexión y sincronice al volver.
4. **Migrar a PostgreSQL** – Para despliegue en producción sin riesgo de perder datos.
5. **Gráficos avanzados** – Integrar Chart.js o Plotly para visualizaciones más ricas.
6. **Notificaciones** – Alertas cuando se supere un umbral diario.
7. **API pública documentada** – Swagger/OpenAPI con Flask-RESTX.
8. **Tests automatizados** – pytest para las rutas de la API.

### Migrar de SQLite a PostgreSQL

```python
# En app.py, cambiar:
import psycopg2
DB_URL = os.environ.get("DATABASE_URL", "postgresql://user:pass@localhost/reciclapp")
```

Y añadir `psycopg2-binary` a `requirements.txt`.

---

## 👥 Equipo de desarrollo

| Nombre | Rol |
|---|---|
| — | Backend Flask / API |
| — | Frontend formulario táctil |
| — | Frontend dashboard |
| — | Base de datos / despliegue |

---

## 📄 Licencia

MIT License – libre para uso educativo y modificación.

---

*Desarrollado en el marco de la actividad de centro de DAM – IES Cuatrovientos*
