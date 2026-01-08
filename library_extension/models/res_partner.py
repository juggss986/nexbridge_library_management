from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    my_book_ids = fields.Many2many(
        string='My Book',
        comodel_name='library.management',
    )
    