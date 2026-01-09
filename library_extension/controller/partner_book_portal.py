from odoo import http
from odoo.http import request

class BookPortal(http.Controller):

    @http.route(['/my/books'], type='http', auth='user', website=True)
    def portal_books(self, **kw):
        partner_books_ids = request.env.user.partner_id.my_book_ids
        books = request.env['library.management'].sudo().search([('id', 'in', partner_books_ids.ids)])
        return request.render(
            'library_extension.partner_portal_books_page',
            {'books': books}
        )
