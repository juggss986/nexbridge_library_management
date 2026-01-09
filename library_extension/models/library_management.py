from odoo import models, fields


class LibraryManagement(models.Model):
    _inherit = "library.management"
    
    book_web_link = fields.Char(string="Wikipage Link")