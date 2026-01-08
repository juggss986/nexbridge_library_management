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

    def validate_isbn(self):
        for rec in self:
            if not rec.isbn:
                raise ValidationError(f"Please provide an ISBN for {rec.title}.")
            try:
                int(rec.isbn)
                isbn = isbnlib.canonical(rec.isbn)
            except Exception:
                raise ValidationError("ISBN must be digits only.")

            if not isbnlib.is_isbn13(isbn):
                raise ValidationError("ISBN must be a valid ISBN-13.")

        # If valid, return success notification
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Validation Successful',
                'message': 'ISBN is valid!',
                'type': 'success',
            }
        }
    
    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.validate_isbn()
        return records

    def write(self, vals):
        res = super().write(vals)
        self.validate_isbn()
        return res
    