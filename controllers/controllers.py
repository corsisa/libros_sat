# -*- coding: utf-8 -*-
from odoo import http

# class LibrosSat(http.Controller):
#     @http.route('/libros_sat/libros_sat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libros_sat/libros_sat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libros_sat.listing', {
#             'root': '/libros_sat/libros_sat',
#             'objects': http.request.env['libros_sat.libros_sat'].search([]),
#         })

#     @http.route('/libros_sat/libros_sat/objects/<model("libros_sat.libros_sat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libros_sat.object', {
#             'object': obj
#         })