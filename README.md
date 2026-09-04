# Odoo 19 Development Environment

Entorno de desarrollo para Odoo 19 utilizando Docker, PostgreSQL y módulos personalizados.

## 📋 Descripción

Este proyecto contiene un entorno local para desarrollar y probar módulos personalizados de Odoo 19 sin modificar directamente el código fuente de Odoo.

La arquitectura utiliza Docker Compose para ejecutar:

* Odoo 19
* PostgreSQL 15
* Addons personalizados

## 🏗️ Arquitectura

```text
Windows
│
├── VS Code
│
└── Docker Desktop
    │
    ├── Odoo 19
    │   └── Puerto 8069
    │
    └── PostgreSQL 15
        └── Base de datos Odoo
```

Los módulos personalizados se encuentran en:

```text
custom-addons/
```

y son montados dentro del contenedor de Odoo en:

```text
/mnt/extra-addons
```

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

> La carpeta `postgres/` contiene los datos de PostgreSQL y está excluida del repositorio mediante `.gitignore`.

## 🐳 Requisitos

Antes de utilizar este proyecto se necesita:

* Windows 10/11
* Docker Desktop
* Git
* Visual Studio Code

## 🚀 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
cd odoo-dev
```

Levantar los servicios:

```bash
docker compose up -d
```

Comprobar los contenedores:

```bash
docker ps
```

Los servicios principales serán:

```text
odoo19
odoo19-postgres
```

## 🌐 Acceso a Odoo

Una vez levantados los contenedores:

```text
http://localhost:8069
```

## 🗄️ Base de datos

El entorno utiliza:

```text
PostgreSQL 15
```

Configuración actual de desarrollo:

```text
Host: db
Puerto: 5432
Usuario: odoo
Base inicial: postgres
```

La base de datos de desarrollo utilizada durante el curso es:

```text
Odo-dev
```

## 🧩 Desarrollo de módulos

Los módulos personalizados deben colocarse dentro de:

```text
custom-addons/
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

## 🔄 Actualizar un módulo

Después de modificar el código, reiniciar el contenedor:

```bash
docker compose restart odoo
```

Para actualizar un módulo desde la terminal:

```bash
docker exec odoo19 odoo -d "Odo-dev" -u curso_odoo --stop-after-init
```

Después volver a iniciar Odoo:

```bash
docker compose up -d
```

## 🧪 Comprobar sintaxis Python

Para comprobar un archivo Python dentro del contenedor:

```bash
docker exec odoo19 python3 -m py_compile /mnt/extra-addons/curso_odoo/models/curso.py
```

Si el comando no devuelve ningún error, la sintaxis Python es válida.

## 📚 Módulos de práctica

### curso_odoo

Primer módulo desarrollado durante el curso de Odoo 19.

Actualmente contiene:

* Modelo `curso.odoo`
* Nombre
* Descripción
* Activo
* Edad
* Precio
* Fecha de inicio
* Relación con `res.partner` mediante `Many2one`
* Vista de lista
* Vista de formulario
* Menús
* Permisos de acceso

## 🛠️ Objetivos del proyecto

El objetivo es utilizar este entorno para aprender y desarrollar:

* Modelos Odoo
* Campos
* ORM
* Vistas XML
* Acciones
* Menús
* Seguridad
* Relaciones entre modelos
* Herencia de modelos
* Automatizaciones
* Reportes
* JavaScript / OWL
* Integraciones mediante API
* Desarrollo de módulos empresariales

## 📌 Regla de desarrollo

No se debe modificar directamente el código fuente de Odoo.

Los desarrollos personalizados deben realizarse mediante módulos dentro de:

```text
custom-addons/
```

## 📄 Licencia

Este repositorio contiene código de desarrollo y aprendizaje para Odoo.

La licencia y condiciones de distribución de cualquier módulo personalizado deberán definirse antes de utilizarlo en producción.
