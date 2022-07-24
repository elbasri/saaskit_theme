from odoo import http
from odoo.http import request

class DetailModule(http.Controller):
    @http.route('/detailmodule', auth='public', website=True):
    def index(self):
        return request.render('theme_odoo.DetailModule')