from odoo import models, fields


class CursoOdoo(models.Model):
    _name = "curso.odoo"
    _description = "Curso Odoo"

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    descripcion = fields.Text(
        string="Descripción",
    )

    activo = fields.Boolean(
        string="Activo",
        default=True,
    )

    edad = fields.Integer(
        string="Edad",
    )

    precio = fields.Float(
        string="Precio",
    )

    fecha_inicio = fields.Date(
        string="Fecha de inicio",
    )
    profesor_id = fields.Many2one(
    "res.partner",
    string="Profesor",
)
    tema_ids = fields.One2many(
    "curso.odoo.tema",
    "curso_id",
    string="Temas",
)