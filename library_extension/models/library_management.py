from odoo import models, fields


class LibraryManagement(models.Model):
    _inherit = "library.management"
    
    book_web_like = fields.Char(string="Wikipage Link")