from odoo import models, fields, api, _, exceptions
import isbnlib

class LibraryManagement(models.Model):
    _name = "library.management"

    title = fields.Char(string="Title", required=True)
    isbn = fields.Char(
        string='ISBN',
        help="Unique13-digit code identifying a specific edition of a book or book-like product"
    )
    date_published = fields.Date(
        string='Date Published',
        default=fields.Date.context_today,
    )
    publisher_id = fields.Many2one(
        string='Publisher',
        comodel_name='res.partner',
    )
    
    authors_ids = fields.Many2many(
        string='Authors',
        comodel_name='res.partner',
    )

    cover_image = fields.Binary(
        string='Cover',
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )

    