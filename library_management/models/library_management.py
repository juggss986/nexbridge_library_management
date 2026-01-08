from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


import isbnlib

class LibraryManagement(models.Model):
    _name = "library.management"
    _rec_name = 'title'
    
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

    def validate_isbn(self):
        for rec in self:
            try:
                int(rec.isbn)
                isbn = isbnlib.canonical(rec.isbn)
            except Exception:
                raise ValidationError("ISBN must be a digit.")

            if not isbnlib.is_isbn13(isbn):
                raise ValidationError("ISBN must be a valid ISBN-13.")

        return True
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'title' not in vals:
                raise ValidationError("Please provide a book name.")
            
            if 'isbn' not in vals or not vals.get('isbn'):
                raise ValidationError(f"Please provide an ISBN for {vals.get('title', '')}.")
        
        return super().create(vals_list)

    def write(self, vals):
        if 'title' in vals and not vals['title']:
            raise ValidationError("Please provide a book name.")\
            
        if 'isbn' in vals and not vals.get('isbn') :
            raise ValidationError(f"Please provide an ISBN for {self.title or ''}.")

        return super().write(vals)
    