# -*- coding: utf-8 -*-
# from odoo import http


# class Abymart(http.Controller):
#     @http.route('/abymart/abymart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abymart/abymart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abymart.listing', {
#             'root': '/abymart/abymart',
#             'objects': http.request.env['abymart.abymart'].search([]),
#         })

#     @http.route('/abymart/abymart/objects/<model("abymart.abymart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abymart.object', {
#             'object': obj
#         })
