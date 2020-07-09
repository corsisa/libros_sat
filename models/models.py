# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libro_ventas_sat(models.Model):
    _name = 'libro.ventas_sat'
    _description = 'Modelo para el libro de venta'

    fecha = fields.Date(string='Fecha',required=True,default=fields.Date.today())
    numeros = fields.Char(string='Num. Facturas',required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='restrict',required=True,)
    serie = fields.Char(string='Serie', required=True)
    tipo_vent = fields.Selection([('1','Bienes'),('2','Servicios')],
                    string='Tipo', default='1')
    origen = fields.Selection([('n', 'Nacional'),('i','Importacion')], 
                    string='Origen',default='n')
    base = fields.Float(string='Sub Total',)
    iva = fields.Float(string='IVA',)
    total = fields.Float(string='Total')
        

    @api.onchange('total')

    def _montos_ventas(self):

        self.base = self.total / 1.12
        self.iva = self.total - (self.total /1.12)

class libro_compras_sat(models.Model):
    _name = 'libro.compras_sat'
    _description = 'Modelo para el libro de Compra'

    fecha = fields.Date(string='Fecha',required=True,default=fields.Date.today())
    numero = fields.Char(string='Num. Facturas',required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='restrict',required=True,)
    serie = fields.Char(string='Serie', required=True)
    tipo_comp = fields.Selection([('1','Bienes'),('2','Servicios')],
                    string='Tipo', default='1')
    origen = fields.Selection([('n', 'Nacional'),('i','Importacion')], 
                    string='Origen',default='n')
    base = fields.Float(string='Sub Total',)
    iva = fields.Float(string='IVA',)
    total = fields.Float(string='Total')
        

    @api.onchange('total')

    def _montos_compras(self):

        self.base = self.total / 1.12
        self.iva = self.total - (self.total /1.12)