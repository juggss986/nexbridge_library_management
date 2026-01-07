from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


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

    _sql_constraints = [
    ('isbn_unique', 'unique(isbn)', 'ISBN must be unique.')
]

    def _validate_isbn(self, isbn):
        try:
            isbn = isbnlib.canonical(isbn)
        except Exception:
            raise ValidationError("Invalid ISBN format.")

        if not isbnlib.is_isbn13(isbn):
            raise ValidationError("ISBN must be a valid ISBN-13.")

        return isbn
    
    
    def create(self, vals):
        if 'isbn' in vals and vals['isbn']:
            vals['isbn'] = self._validate_isbn(vals['isbn'])
        return super().create(vals)

    def write(self, vals):
        if 'isbn' in vals and vals['isbn']:
            vals['isbn'] = self._validate_isbn(vals['isbn'])

        
        return super().write(vals)
    