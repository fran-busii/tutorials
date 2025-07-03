# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Quotation_invnumber(models.Model):
     _inherit = 'sale.order'
     _description = 'add invoice number to quotation'
    
     