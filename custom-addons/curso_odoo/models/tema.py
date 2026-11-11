from odoo import models, fields


class CursoOdooTema(models.Model):
    _name = "curso.odoo.tema"
    _description = "Tema del Curso"

    name = fields.Char(
        string="Tema",
        required=True,
    )

    descripcion = fields.Text(
        string="Descripción",
    )

    orden = fields.Integer(
        string="Orden",
        default=10,
    )

    curso_id = fields.Many2one(
        "curso.odoo",
        string="Curso",
        required=True,
        ondelete="cascade",
    )