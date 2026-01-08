
from odoo import http
from odoo.http import request

class ControllerName(http.Controller):
    """
        Routes:
          /library/books: controller for displaying recorded books in the library.
    """

    @http.route(['/library/books'], auth='public', type='http', website=True)
    def portal_books(self, **kw):
        book_ids = request.env['library.management'].search([('active', '=', True)])
        values = {
            'books': book_ids,
        }
        
        return request.render("library_management.portal_books", values)
