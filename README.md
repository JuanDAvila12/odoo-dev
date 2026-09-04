# Odoo 19 Development Environment

Entorno de desarrollo para **Odoo 19** utilizando Docker, PostgreSQL y módulos personalizados.

Repositorio:

**https://github.com/JuanDAvila12/odoo-dev**

---

## 📋 Descripción

Este proyecto contiene un entorno local para desarrollar y probar módulos personalizados de Odoo 19 sin modificar directamente el código fuente de Odoo.

El objetivo es disponer de un laboratorio de desarrollo reproducible para aprender Odoo y construir funcionalidades empresariales personalizadas.

---

## 🏗️ Arquitectura

```text
Windows
│
├── Visual Studio Code
│
└── Docker Desktop
    │
    ├── Odoo 19
    │   └── Puerto 8069
    │
    └── PostgreSQL 15
        └── Base de datos Odoo
```

### Servicios

| Servicio      | Tecnología    | Puerto |
| ------------- | ------------- | -----: |
| Odoo          | Odoo 19       |   8069 |
| Base de datos | PostgreSQL 15 |   5432 |

---

## 📁 Estructura del proyecto

```text
odoo-dev/
│
├── README.md
├── .gitignore
├── docker-compose.yml
│
├── config/
│
├── custom-addons/
│   └── curso_odoo/
│       ├── __init__.py
│       ├── __manifest__.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── curso.py
│       │
│       ├── views/
│       │   └── curso_views.xml
│       │
│       └── security/
│           └── ir.model.access.csv
│
└── postgres/
```

> La carpeta `postgres/` contiene los datos locales de PostgreSQL y está excluida del repositorio mediante `.gitignore`.

---

## 🐳 Requisitos

Para utilizar este entorno se requiere:

* Windows 10/11
* Docker Desktop
* Git
* Visual Studio Code

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JuanDAvila12/odoo-dev.git
cd odoo-dev
```

### 2. Levantar Odoo y PostgreSQL

```bash
docker compose up -d
```

### 3. Comprobar los contenedores

```bash
docker ps
```

Deben aparecer:

```text
odoo19
odoo19-postgres
```

### 4. Acceder a Odoo

Abrir en el navegador:

```text
http://localhost:8069
```

---

## 🗄️ Base de datos

El entorno utiliza:

```text
PostgreSQL 15
```

Configuración del contenedor:

```text
Host: db
Puerto: 5432
Usuario: odoo
Contraseña: odoo
```

La base de datos de desarrollo utilizada actualmente es:

```text
Odo-dev
```

> Las credenciales anteriores son únicamente para el entorno local de desarrollo. No deben utilizarse en producción.

---

## 🧩 Desarrollo de módulos

Los módulos personalizados se almacenan en:

```text
custom-addons/
```

y se montan dentro del contenedor de Odoo en:

```text
/mnt/extra-addons
```

Ejemplo:

```text
custom-addons/
└── mi_modulo/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    ├── views/
    └── security/
```

---

# 📚 Módulo actual: curso_odoo

El primer módulo desarrollado dentro de este proyecto.

## Modelo

```text
curso.odoo
```

## Campos actuales

```text
name
descripcion
activo
edad
precio
fecha_inicio
profesor_id
```

## Relaciones

El campo:

```text
profesor_id
```

es una relación `Many2one` hacia:

```text
res.partner
```

Esto permite seleccionar un contacto de Odoo como profesor del curso.

## Funcionalidades actuales

* Modelo personalizado
* Campos básicos
* Campo booleano
* Fecha
* Entero
* Decimal
* Relación `Many2one`
* Vista de lista
* Vista de formulario
* Acción de ventana
* Menú personalizado
* Permisos de acceso

---

## 🔄 Flujo de desarrollo

El flujo utilizado en este proyecto es:

```text
Modificar código
      ↓
Guardar cambios
      ↓
Reiniciar Odoo
      ↓
Actualizar módulo
      ↓
Probar en Odoo
      ↓
Corregir errores
      ↓
Git commit
      ↓
Git push
```

---

## 🔧 Comandos útiles

### Iniciar Odoo

```bash
docker compose up -d
```

### Detener los servicios

```bash
docker compose down
```

### Reiniciar Odoo

```bash
docker compose restart odoo
```

### Ver contenedores

```bash
docker ps
```

### Ver logs de Odoo

```bash
docker logs odoo19 --tail 100
```

### Ver logs en tiempo real

```bash
docker logs -f odoo19
```

### Comprobar sintaxis Python

```bash
docker exec odoo19 python3 -m py_compile /mnt/extra-addons/curso_odoo/models/curso.py
```

### Actualizar el módulo

```bash
docker exec odoo19 odoo -d "Odo-dev" -u curso_odoo --stop-after-init
```

Después:

```bash
docker compose up -d
```

---

## 🔐 Seguridad

Nunca se deben subir al repositorio:

```text
.env
.env.*
postgres/
*.log
credenciales
claves API
contraseñas de producción
```

El archivo `.gitignore` está configurado para excluir estos elementos.

---

## 🎯 Objetivos del proyecto

Este repositorio será utilizado para aprender y desarrollar:

* Modelos Odoo
* Campos
* ORM
* Vistas XML
* Acciones
* Menús
* Seguridad
* `Many2one`
* `One2many`
* `Many2many`
* Herencia de modelos
* Herencia de vistas
* Automatizaciones
* Campos calculados
* Reportes
* JavaScript / OWL
* Integraciones mediante API
* Desarrollo de módulos empresariales
* Git y GitHub
* Despliegue en producción

---

## 🏢 Próximos desarrollos

El objetivo a largo plazo es utilizar los conocimientos adquiridos en este entorno para desarrollar funcionalidades empresariales, incluyendo:

* Gestión de productos
* Inventarios
* Almacenes
* Compras
* Ventas
* Contabilidad
* Reportes
* Control de ciclo de vida de productos
* Automatizaciones empresariales
* Integraciones con sistemas externos

---

## 📖 Curso de desarrollo Odoo 19

Este repositorio forma parte de un aprendizaje práctico de desarrollo en Odoo 19.

La progresión prevista es:

```text
Clase 1  → Preparación del entorno
Clase 2  → Arquitectura de Odoo
Clase 3  → Primer módulo
Clase 4  → Modelos y campos
Clase 5  → Relaciones entre modelos
Clase 6  → Vistas XML
Clase 7  → Seguridad
Clase 8  → ORM
Clase 9  → Herencia
Clase 10 → Automatizaciones
Clase 11 → Reportes
Clase 12 → OWL / JavaScript
Clase 13 → APIs
Clase 14 → Git y GitHub
Clase 15 → Producción
```

---

## 📌 Regla de desarrollo

Los desarrollos personalizados deben realizarse mediante módulos dentro de:

```text
custom-addons/
```

No se debe modificar directamente el código fuente de Odoo.

Esto permite mantener los desarrollos separados del núcleo de Odoo y facilita futuras actualizaciones.

---

## 📄 Estado actual

**Entorno:** Desarrollo local
**Odoo:** 19
**PostgreSQL:** 15
**Docker:** Docker Compose
**Estado:** En desarrollo

---

## 👨‍💻 Autor

**Juan Luis**

Repositorio:

**https://github.com/JuanDAvila12/odoo-dev**
