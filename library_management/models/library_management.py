from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


import isbnlib

class LibraryManagement(models.Model):
    _name = "library.management"

    title = fields.Char(string="Title")
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

    def validate_isbn(self):
        for rec in self:
            try:
                isbn = isbnlib.canonical(rec.isbn)
            except Exception:
                raise ValidationError("Invalid ISBN format.")

            if not isbnlib.is_isbn13(isbn):
                raise ValidationError("ISBN must be a valid ISBN-13.")

        return True
    
    
    def create(self, vals):
        if 'title' not in vals:
            raise ValidationError("Please provide a book name.")
        
        return super().create(vals)

    def write(self, vals):
        if 'title' in vals and not vals['title']:
            raise ValidationError("Please provide a book name.")

        return super().write(vals)
    