{
    "name": "Curso Odoo",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "summary": "Mi primer módulo de desarrollo en Odoo",
    "description": """
        Módulo creado durante el curso de desarrollo Odoo 19.
    """,
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/curso_views.xml",
    ],
    "installable": True,
    "application": True,
}