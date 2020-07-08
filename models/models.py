# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libros_sat(models.Model):
    _name = 'libros.libros_sat'

    fecha = fields.Date(string='Fecha',required=True,default=fields.Date.today())
    numeros = fields.Char(string='Num. Facturas',required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='restrict',required=True,)
    serie = fields.Char(string='Serie', required=True)
    tipo = fields.Selection([('1','Bienes'),('2','Servicios')])
    base = fields.Float(string='Sub Total',)
    iva = fields.Float(string='IVA',)
    total = fields.Float(string='Total')
        

    @api.onchange('total')

    def _onchange_montos(self):

        self.base = self.total / 1.12
        self.iva = self.total - (self.total /1.12)