# -*- coding: utf-8 -*-
from openerp import http

# class CheckVaucherDo(http.Controller):
#     @http.route('/check_vaucher_do/check_vaucher_do/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_vaucher_do/check_vaucher_do/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_vaucher_do.listing', {
#             'root': '/check_vaucher_do/check_vaucher_do',
#             'objects': http.request.env['check_vaucher_do.check_vaucher_do'].search([]),
#         })

#     @http.route('/check_vaucher_do/check_vaucher_do/objects/<model("check_vaucher_do.check_vaucher_do"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_vaucher_do.object', {
#             'object': obj
#         })